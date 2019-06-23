title: Generating fake whiskey reviews with GPT-2
slug: whiskey-reviews
date: 2019-06-23 19:00:00 UTC+01:00
tags: python, deep learning, natural language
category: 
cover: images/robot-whiskey.jpg
link: 
status: 
description:
type: text
author: John Paton
summary: I've enjoyed whiskey for a while now, but I can never vocalize all the flavors present in a bottle. I read all these flowery reviews and tasting notes online and I just have no idea how these people come up with [descriptions like](http://whiskyadvocate.com/ratings-reviews/?search=Johnnie+Walker+Blue+Label&submit=+&brand_id=0&rating=0&price=0&category=0&styles_id=0&issue_id=0) "caramels, dried peats, elegant cigar smoke, seeds scraped from vanilla beans, brand new pencils, peppercorn, coriander seeds, and star anise"... until now. 

I've enjoyed whiskey for a while now, but I can never vocalize all the flavors present in a bottle. I read all these flowery reviews and tasting notes online and I just have no idea how these people come up with [descriptions like](http://whiskyadvocate.com/ratings-reviews/?search=Johnnie+Walker+Blue+Label&submit=+&brand_id=0&rating=0&price=0&category=0&styles_id=0&issue_id=0) "caramels, dried peats, elegant cigar smoke, seeds scraped from vanilla beans, brand new pencils, peppercorn, coriander seeds, and star anise"... until now. 

* [The data](#the-data)
* [Fine-tuning GPT-2](#fine-tuning)
* [Fake whiskey reviews](#fake-reviews)
* [Highlights](#highlights)
* [Bloopers](#bloopers)

[OpenAI](https://openai.com/) recently made headlines with their blog post [Better Language Models and Their Implications](https://openai.com/blog/better-language-models/), in which they described their latest general language model, dubbed [GPT-2](https://d4mucfpksywv.cloudfront.net/better-language-models/language-models.pdf). In the post, they claim to be practicing responsible (non)disclosure by not releasing the full pre-trained model due to concerns that it is so good, it could be used for fake news generation or social media manipulation. However, they _did_ release smaller versions of the model which are nonetheless still quite performant. You can play with one of them at [talktotransformer.com](https://talktotransformer.com/). 

Obviously this piqued my interest. I've dabbled in [purposely _bad_ language generation](https://johnpaton.net/posts/engl_ish/), but this time I was curious about doing something vaguely believable. I decided to try to sound more impressive in my whiskey-ing by generating my very own fake whiskey reviews, fine-tuning the small version of GPT-2 on existing reviews.

<img style="max-height: 350px" src="/images/robot-whiskey.jpg" alt="Robot hand holding whiskey">
<div style="text-align:center"><small> Image by the <a href="https://nypost.com/2019/05/14/microsoft-partners-with-distillery-to-create-worlds-first-ai-whiskey/">New York Post</a> </small></div>


<a id='the-data'></a>
## The data

The first site on Google when I searched for "whiskey reviews" was [whiskyadvocate.com](http://whiskyadvocate.com/), and it seemed perfect for my needs. Short, consistently formatted reviews, and all on one long page making them easy to scrape. 

The only snag is that you have to click a "See More" button over and over to get 6 more reviews to render each time. I know you can use sophisticated scraping tools to deal with this situation, but I decided that that would be overkill for this project. Luckily I've been JavaScripting a little bit recently so it occurred to me that you can pop open the browser console and run:

```javascript
> var btn = document.getElementById("loadMore")
> for (var i = 0; i < 100; i++) {btn.click();};
```

After glitching out for a bit, the whole set of reviews is visible on the page. One `ctrl+S` and we have the reviews ready for parsing with `beautifulsoup`. Looking at the html, we see that each review is in its own `<article>` block, so they are easy enough to extract:

```python
from bs4 import BeautifulSoup
with open("data/raw/whisky_advocate.html") as h:
    raw_data = h.read()
soup = BeautifulSoup(raw_data)
articles = soup.findAll("article")
```

Checking out the text structure of one "article", that all we really need to do to clean up is drop empty lines and replace non-breaking spaces (`/xa0`) with normal ones.

```python
reviews_clean = []
for a in articles:
    a_clean = [
        line.replace("\xa0", " ")  # breaking spaces
        for line in a.text.split("\n") 
        if line is not ''  # drop empty lines
    ]
    # rejoin into one formatted snipped
    reviews_clean.append("\n".join(a_clean)) 
```

This gives us nice clean review snippets in the following format:

>**Real Review (input data)**
>
>95 points
>
>Uncle Nearest 1820 Single Barrel 11 year old Tennessee Whiskey (Barrel US-2), 55.1%
>
>Bourbon/Tennessee  |  $119
>
>This is mature whiskey at its most refined: a balance of fruits, nuts, sweetness, and restrained oak. The nose has it all: salted, buttered pecans, rock candy, Dr. Pepper, blackberry jam, dried blueberries, caramel corn, tobacco barn, and old leather chair. It’s practically dessert-like in the mouth, with dark chocolate-covered caramel, candied pecans, Goo Goo Clusters, cherry cola, blackberry and blueberry jam, and a kiss of white pepper. The finish stays consistent, a mouthwatering mélange of caramel, chocolate, and nuts. Harmonious, seamless, and silky—you’d never guess the proof.

Looks (and sounds) good to me! The last step is to save out reviews back to a text file for processing by GPT-2. The model distinguishes between separate pieces of text using a special token, `<|endoftext|>`. So we join all the reviews back together, separated by this token, and save it to a text file:

```python
with open("data/clean/reviews.txt", "w") as h:
    output = "\n<|endoftext|>\n".join(reviews_clean)
    h.write(output+"\n")
```

Now we're ready to train!

After training the model, it turned out I was only using the [Summer 2019 Buying Guide](http://whiskyadvocate.com/ratings-reviews/?search=&submit=&brand_id=0&rating=0&price=0&category=0&styles_id=0&issue_id=102) and not the full set of reviews, so there is definitely room for improvement here. 

<a id='fine-tuning'></a>
## Fine-tuning GPT-2

Surprisingly, this is actually the easy part, thanks to work by [nshepperd](https://github.com/nshepperd). His/her [fork of GPT-2](https://github.com/nshepperd/gpt-2) contains a super easy train script for finetuning GPT-2, with lots of options. To get started with it, we clone the repo and use the provided script to download the pre-trained model. This model has already been trained on a set of [8 million web pages](https://openai.com/blog/better-language-models/#fn1), so it already has a pretty big and diverse vocabulary. We'll download the smaller model, called `117M`:

```bash
$ git clone https://github.com/nshepperd/gpt-2.git
$ cd gpt-2 
$ pip3 install -r requirements.txt 
$ python3 download_model.py 117M
```

This will save the pre-trained model in the `models` directory.

The set of reviews isn't very big (the whole site contains about 4,000, but I only grabbed 125 during this experiment due to the mistake mentioned above), so this will be less like fine-tuning and more like clobbering the model. When we are done, it will know nothing but whiskey reviews. For that reason, we output samples frequently during training, with the expectation that the sweet-spot for interesting new reviews will come somewhere before the model is totally overfit. 

With our processed reviews in `data/clean/reviews.txt`, we run the training script on our data, setting the `PYTHONPATH` variable as indicated in the [readme](https://github.com/nshepperd/gpt-2#fine-tuning-on-custom-datasets). We output 30 samples every 25 epochs, with a length of 250 words (long enough that a full review should fit in there). We also checkpoint the model at that point so that we can return to it to generate more samples later if we want:

```bash
$ PYTHONPATH=gpt-2/src python3 gpt-2/train.py \
      --dataset data/clean/reviews.txt \
      --save_every 25 --sample_every 25 \
      --sample_length 250 --sample_num 30
```

The script will create a `samples` directory and save the samples there, and also a `checkpoints` directory. It runs until you kill it with `ctrl+C`, so feel free to go get a coffee.

<a id='fake-reviews'></a>
## Fake whiskey reviews

The first thing to notice about the output is that the generated text is usually really coherent at first glance. After 25 epochs, the model isn't really talking about whiskey yet, so we mostly get a peek into the kind of text generation that it's capable of:

>**GPT-2 SAMPLE: 25 Epochs**
>
>We are pleased to present the third of over 1,000 stories published by the New England Journal of Medicine, from all continents. The authors have collected information on over 50,000 individuals in the United States who were examined at the National Heart, Lung and Blood Institute (NHBI) and included information on symptoms and treatments. The research was focused on coronary artery bypass grafting, cardiovascular dysfunction, cardiovascular disease, and coronary artery disease.
>
>For complete details and results, visit <a href="http://www.nlm.nih.gov/pubmed/257720" style="word-wrap : break-word;">http://www.nlm.nih.gov/pubmed/257720</a>.


The URL doesn't work, I checked. This is generated text. 

After 50 epochs, we're already seeing some promising output, though there's definitely work to do:

>**GPT-2 SAMPLE: 50 Epochs**
>
>The packaging is as it should be: it looks fine (with more sugar than water), but the nose gets burnt out, which can be remedied with some honey. There were a couple of more hints of red wine and chocolate, but in the nose this gives way to a more complex whisky with plenty of chocolate and dried fruit. On the palate, it's just perfect. The nose is quite dry and mouthful, but more like a whisky where, when you pour it into your mouth and add it, you find the sweetness of cherry-chardonnay, fresh orange peel, ginger, and vanilla peel. On the palate, it develops chocolate, vanilla syrup, and nutmeg, along with a light and pleasant hint of dried fruit, then is broken up by chocolate, cherry, and pepper notes. Very well-designed, although this was not finished in time.
>
>1/5

At 100 epochs, we have a review that at first glance seems reasonable:

>**GPT-2 SAMPLE: 100 Epochs**
>
>85 points
>
>Black Cherry Ale, 90%
>
> Blended Malt Whisky  |  $60
>
> The nose was very light and crisp, with chocolate, banana candy flavor, honey, espresso, toffee, and herbal aromas. The palate was warm, with vanilla, cinnamon, and chocolate sweetness. The finish was medium in length, with plenty of vanilla and chocolate, and the finish was strong and well-balanced: chocolate, caramel, milk chocolate, milk chocolate, caramel, and sweet almond.                        

Note that the model is even mimicking our formatting. This one ticks all the boxes of a review, but check out the tasting notes: vanilla, cinnamon, chocolate, caramel, sweet almond. There's definitely a theme: these are baking ingredients! Many food words are used in tasting notes. The model is learning this, but the text it was trained on seems to have included many recipes, as all sorts of baking instructions are also being generated. This was another sample from the same batch:

>**GPT-2 SAMPLE: 100 Epochs**
>
>1 pint brown sugar
>
>1 egg, beaten
>
>1 teaspoon kosher salt
>
>3 ounces butter, softened
>
>3 egg whites, beaten
>
>12 drops honey, at room temperature
>
>2 tablespoons brown sugar/butter
>
>3 tablespoons apple cider vinegar, at room temperature
>
>2 tablespoons powdered pepper
>
>1/2 teaspoon pepper
>
>1 tablespoon black pepper
>
>Directions
>
>1. In a medium bowl, beat butter, 1/2 cup apple cider vinegar, and vanilla until smooth, 2-4 hours. Add in egg whites, and gradually add more egg whites, if needed. (You may need to add more milk and so forth.)
>
>2. Pour milk/soy mixture through an egg grinder; if it is hard, you might have to do it some more. If there isn't quite so much water, you're going to have to let the milk drain on the stove top.
>
>3. Add water once, once or twice, until all the water is dissolved, about 3-4 hours. Add pepper, egg whites, vanilla, and water.
>
>4. Whisk in egg shells and water; the water gets very sticky; add salt

"Pour milk/soy mixture through an egg grinder; if it is hard, you might have to do it some more" isn't exactly sensible, but it is definitely coherent and the whole thing reads like a recipe. Just don't try it at home. 

After 200 epochs, the model is producing whiskey reviews that I (as a layman) can't distinguish from the real thing:

>**GPT-2 SAMPLE: 200 Epochs**
>
>91 points
>
>Luxembourg 60 year old (Batch 2), 59%
>
>Single Malt Scotch  |  $235
>
>Quite simply the most beautiful whisky in Europe at the time. Beautifully balanced spices, herbal oloroso fruits, soft earthy aromas of honey, licorice, lavender, lavender oil, and a hint of espresso. The palate is rich and richly spiced, with dark tannins, orange candy, green bananas, almond milk, espresso, brown sugar, and cream cheese louis. Floral notes and honeycomb in the finish. (12,800 bottles for U.S.)

However, it is also revealing one of GPT-2's flaws: it has a tendency to abruptly switch context, which can be quite comical. From the same batch:

>**GPT-2 SAMPLE: 200 Epochs**
>
> A group of scientists led by Professor Jonny Wilkinson has found that the planet Saturn has the highest amount of formaldehyde on Earth. The concentration falls short, with only slightly more than 100 parts per million of the general background. It is 80 parts per million in the form of sisphenol A (s<3 parts per million<30 parts per million): this is also found in less-drying water like water and soda water. The taste is more palatable, with more of both honey and orange, then chocolate hazelnut, vanilla pod, chocolate chip cookies, caramel, hazelnut, coconut, and a sprinkling of orange oil. There are also more dark chocolate aromas, which are sweeter and with some spice and nutmeg addition. One might expect there to be more chocolate, but, on closer inspection, it's more fruitcake and chocolate barristers will ultimately find it all.

and:
  
>**GPT-2 SAMPLE: 200 Epochs**
>
>90 points
>
>Lemon Keg, 57%
>
>Japanese  |  $45
>
>The standard edition features a black leather jacket with leather cuffs and white floral print buttons. The back has a floral feel, but is made from milk chocolate; the outside shell lacks much citrus or sweetness, which ultimately leads to a light taupe hue and ample mouth-drawing.

This is also what I meant by clobbering the model: it is forgetting how to remain in other contexts. No matter where it starts, it is beginning to see everything as a whiskey review. By this point most (but not all) of the samples are also formatted like our whiskey reviews. This distinctive formatting proved to be a very useful tool in gauging to what extent we were overfitting the model.

By about 250 epochs, most of the output is pretty believable, with the only consistent flaw being repeated flavors in the tasting notes. All in all, I was surprised at both how easy the open source community made this experiment, and also how quickly and accurately the model was able to start replicating reasonable-sounding reviews (training only took about a minute per epoch on my old-ish MacBook Pro).

This post is getting long enough, but I'll end with some highlights and bloopers:

<a id='highlights'></a>
## Highlights

Consistency in country of origin (Canadian) and location of distillery (Banff):

>**GPT-2 SAMPLE**
>
>87 points
>
>Millstone 92 Rye, 46%
>
>Canadian  |  $99
>
>The second installment in our four-part rye limited-edition comparison, this proof-bodied reissue from the Millstone Works facility in Banff presents both dry and wet grasses with great maturity. The nose shifts to vanilla, honey, cinnamon, orange oil, licorice, and crystalized halvah. The palate is light and delicate, with nuttiness, cloves, green apple, bitter chocolate, pecan pie, caramel, and bittersweet chocolate. The finish yields leather, honey, roasted nuts, orange, dried citrus, subtle oak, and dried coriander, all evocative of a wartime log. Editors' Choice

Sweet and smooth:

>**GPT-2 SAMPLE**
>
>92 points
>
>Timersley's Barrel-Aged Bourbon, 44%
>
>Blended Scotch Whiskey  |  $30
>
>Sweet potato, strawberry jam, milk chocolate, candies, and brown sugar flavors on the nose, along with smoky bowers & sounders, all wrapped tightly in a viscous, creamy feel. The palate is smooth and gentle, delivering gentle, medium-bodied whiskeys with their own distinctive flavors. A light, nimble palate serves enough sweetness without too much rancor that it becomes sultry, with hot chocolate, strawberry jam, milk chocolate, plum, and cassis.

<a id='bloopers'></a>
## Bloopers

My absolute favorite:

>**GPT-2 SAMPLE**
>
>A smallpox-infected grain, this first-generation proof has a floral, sweet nose laced with blueberry jam, cherry Cask Whisky, toffee, cedar, and tangy oak. It is fragrant and flavorful beyond any description—like a symphony show from before the age of antibiotics.

Whiskey, cigars, or promiscuous McDonald's enthusiasts?

>**GPT-2 SAMPLE**
>
> Twip | 18k Batch | Filch |  |  $75
>
>Makes a delicious mixing bowl of Chocolate Fudge, Big Mac, Ham, Sweet and Sour Apple Cider, Peanuts, and Sour Cream, with a fondness of making out with other people. The caramel is so strong, in fact, that I could only inhale the delicious caramel trails in my cigar box. The only hint I have of burnt sugar and caramel are lost along the way. Sweet and fruity, at least for the $75 price point.

Confusion between whiskey and... pop metal?

>**GPT-2 SAMPLE**
>
>the Chinese pop-metal king Ping'i Minbar began producing small batches for his mouth. Now in its 40s, with a nose of chocolate flan, hedonian, and bubble gum, it ends on sweet and savory rye, with vanilla, orange, and clove. It’s a reprise of the year loaded with floral notes, tangerine, cinnamon, black pepper, and orange soda pop. Floral, earthy, and smoky throughout, this period’s reasonably priced—$120—but well-balanced to give (or withhold) indulgence.

Peanut butter jelly time[:](https://www.youtube.com/watch?v=s8MDNFaGfT4)

>**GPT-2 SAMPLE**
>
>61 points
>
>Chicken Pot Pie with Peanuts, Hot Chocolate, and More Peanuts, 50/50
>
>Single Malt Scotch Whisky  |  $35
>
>Measurable, with portmoking salt water, toasted nuts, caramel, and spices in a thin blanket of peanut butter and jelly, but the panning process was not without its pique. The peanuts and the generous whiskily cooked nuts create an intriguing, if somewhat overcomplicated, vivacious ode to peanut butter and jelly, with sweet peanut butter and jelly, along the way.

What would this even taste like?

>**GPT-2 SAMPLE**
>
>Bourbon/Tennessee  |  $85
>
>Tastes like a young William Shatner novel: rich with flavor, packed with fruit, honey, orange, maple syrup, and aromas of strawberry, licorice, and chocolate, balanced against a lingering tannin of the herbaceous nectar source. The palate is luxurious, richly notes a childhood home.

*Note:* I have kept the generated reviews true to their original formatting and content, with the exception of removing the "Reviewed By" line that WhiskyAdvocate have at the end of their reviews. The model very quickly learned to use the real names of the reviewers, and I didn't want a real person being accused of describing a whiskey as "smallpox-infected".

Thanks to [WhiskyAdvocate](http://whiskyadvocate.com/) for agreeing to let me use their reviews for this post!