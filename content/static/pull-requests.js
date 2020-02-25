function prlist_li(pr){
    // /(owner/repo-name)/pull/(1234)/....
    var re = new RegExp("\/(.+\/.+)\/pull\/([0-9]+)\/?.*$")

    var url = new URL(pr.html_url);
    var repo = re.exec(url.pathname)[1];
    var number = re.exec(url.pathname)[2];

    var name = repo + " #" + number;

    var a = document.createElement("a");
    a.appendChild(document.createTextNode(name));
    a.setAttribute("href", url.href);

    var li = document.createElement("li");
    li.appendChild(a);
    return li
}

function append_if_stars(ul, pr, min_stars){
    var req = new XMLHttpRequest();
    var repo_url = pr.repository_url;
    var msnry = new Masonry(".grid");


    req.onload = function () {
        var stars = JSON.parse(req.responseText).stargazers_count;
        if (stars >= min_stars) {
            ul.appendChild(prlist_li(pr));
            msnry.layout();
        };
    };

    req.open("GET", repo_url);
    req.send();
};

// Set up our HTTP request
var xhr = new XMLHttpRequest();

// Setup our listener to process completed requests
xhr.onload = function () {

    var min_stars = 12;

    // Process our return data
    if (xhr.status >= 200 && xhr.status < 300) {
        var pulls = JSON.parse(xhr.responseText).items
        var prdisplay = document.getElementById("pr-list")

        for (var i = 0; i < pulls.length; i++) {
            var pr = pulls[i];
            append_if_stars(prdisplay, pr, min_stars)
        }
    } else {
        // What do when the request fails
        console.log('The request failed!');
    }    
};

// Create and send a GET request
// The first argument is the post type (GET, POST, PUT, DELETE, etc.)
// The second argument is the endpoint URL
xhr.open('GET', 'https://api.github.com/search/issues?q=is:pr+is:merged+author:johnpaton&sort=created&order=desc');
xhr.send();
