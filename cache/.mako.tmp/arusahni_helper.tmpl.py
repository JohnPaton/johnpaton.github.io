# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496046521.6984227
_enable_loop = True
_template_filename = 'themes/zen/templates/arusahni_helper.tmpl'
_template_uri = 'arusahni_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'html_stylesheets', 'late_load_js', 'html_title', 'html_translations', 'html_tags', 'html_navigation_links', 'html_feedlinks', 'html_sourcelink']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_stylesheets():
            return render_html_stylesheets(context)
        blog_title = context.get('blog_title', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        title = context.get('title', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        is_rtl = context.get('is_rtl', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html\r\n')
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']) or (comment_system == 'facebook'):
            __M_writer("prefix='")
            if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
                __M_writer('og: http://ogp.me/ns# ')
            if use_open_graph:
                __M_writer('article: http://ogp.me/ns/article# ')
            if comment_system == 'facebook':
                __M_writer('fb: http://ogp.me/ns/fb# ')
            __M_writer("'")
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\r\n    <head>\r\n    <meta charset="utf-8">\r\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(str(description))
            __M_writer('">\r\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\r\n    <title>')
        __M_writer(striphtml(str(title)))
        __M_writer(' | ')
        __M_writer(striphtml(str(blog_title)))
        __M_writer('</title>\r\n\r\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\r\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\r\n')
        if permalink:
            __M_writer('      <link rel="canonical" href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\r\n')
        __M_writer('\r\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\r\n')
        __M_writer('\r\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\r\n')
        __M_writer('\r\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="//html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\r\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="/assets/js/html5.js"></script><![endif]-->\r\n')
        __M_writer('\r\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        notes = context.get('notes', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href=\'//fonts.googleapis.com/css?family=Bitter:400,400italic,700\' rel=\'stylesheet\' type=\'text/css\'>\r\n            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\r\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\r\n')
        else:
            if use_cdn:
                __M_writer("            <link href='//fonts.googleapis.com/css?family=Bitter:400,400italic,700' rel='stylesheet' type='text/css'>\r\n")
            else:
                __M_writer('            <link href="/assets/css/bitter.css" rel="stylesheet" type="text/css">\r\n')
            __M_writer('        <link href="/assets/css/main.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\r\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\r\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\r\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\r\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer('        ')
            __M_writer(str(notes.css()))
            __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\r\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\r\n')
            else:
                __M_writer('            <script src="/assets/js/all-nocdn.js" type="text/javascript"></script>\r\n')
        else:
            if use_cdn:
                __M_writer('            <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>\r\n            <script src="//cdnjs.cloudflare.com/ajax/libs/jquery-timeago/1.1.0/jquery.timeago.min.js"></script>\r\n')
            else:
                __M_writer('            <script src="/assets/js/jquery-1.10.2.min.js" type="text/javascript"></script>\r\n            <script src="/assets/js/jquery.timeago.js" type="text/javascript"></script>\r\n')
        __M_writer('    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_title(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        title = context.get('title', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        lang = context.get('lang', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if len(translations) > 1:
            for langname in translations.keys():
                if langname != lang and post.is_translation_available(langname):
                    __M_writer('                <a href="')
                    __M_writer(str(post.permalink(langname)))
                    __M_writer('" rel="alternate" hreflang="')
                    __M_writer(str(langname))
                    __M_writer('">\r\n                ')
                    __M_writer(str(messages("LANGUAGE", langname)))
                    __M_writer('</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if post.tags:
            __M_writer('        <div itemprop="keywords" class="tags">\r\n        <ul>\r\n        ')
            __M_writer(str(messages("Tags")))
            __M_writer('&nbsp;:&nbsp;\r\n')
            for tag in post.tags:
                __M_writer('           <li><a class="tag p-category" href="')
                __M_writer(str(_link('tag', tag)))
                __M_writer('" rel="tag">')
                __M_writer(str(tag))
                __M_writer('</a></li>\r\n')
            __M_writer('        </ul>\r\n        </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        navigation_links = context.get('navigation_links', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        rel_link = context.get('rel_link', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        for url, text, icon in navigation_links[lang]:
            if rel_link(permalink, url) == "#":
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\r\n')
            else:
                __M_writer('            <li><a href="')
                __M_writer(str(url))
                __M_writer('" title="')
                __M_writer(str(text))
                __M_writer('"><i class="')
                __M_writer(str(icon))
                __M_writer('"></i></a></li>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\r\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in translations:
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\r\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if show_sourcelink:
            __M_writer('        &nbsp;&nbsp;|&nbsp;&nbsp;\r\n        <a href="')
            __M_writer(str(post.source_link()))
            __M_writer('" id="sourcelink">')
            __M_writer(str(messages("Source")))
            __M_writer('</a>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 57, "22": 85, "23": 105, "24": 119, "25": 129, "26": 143, "27": 150, "28": 161, "29": 168, "35": 3, "58": 3, "59": 7, "60": 8, "61": 9, "62": 10, "63": 12, "64": 13, "65": 15, "66": 16, "67": 18, "68": 21, "69": 22, "70": 25, "71": 25, "72": 25, "73": 28, "74": 29, "75": 29, "76": 29, "77": 31, "78": 32, "79": 32, "80": 32, "81": 32, "82": 34, "83": 34, "84": 35, "85": 35, "86": 36, "87": 37, "88": 37, "89": 37, "90": 39, "91": 40, "92": 41, "93": 42, "94": 42, "95": 42, "96": 42, "97": 42, "98": 42, "99": 42, "100": 45, "101": 46, "102": 47, "103": 47, "104": 47, "105": 49, "106": 50, "107": 51, "108": 52, "109": 53, "110": 55, "111": 56, "112": 56, "118": 59, "128": 59, "129": 60, "130": 61, "131": 62, "132": 64, "133": 65, "134": 67, "135": 68, "136": 69, "137": 70, "138": 71, "139": 73, "140": 76, "141": 77, "142": 80, "143": 81, "144": 81, "145": 81, "146": 82, "147": 83, "148": 83, "149": 83, "155": 87, "162": 87, "163": 88, "164": 89, "165": 90, "166": 92, "167": 93, "168": 95, "169": 96, "170": 97, "171": 99, "172": 100, "173": 104, "174": 104, "175": 104, "181": 146, "187": 146, "188": 147, "189": 148, "190": 148, "191": 148, "197": 152, "205": 152, "206": 153, "207": 154, "208": 155, "209": 156, "210": 156, "211": 156, "212": 156, "213": 156, "214": 157, "215": 157, "221": 132, "227": 132, "228": 133, "229": 134, "230": 136, "231": 136, "232": 137, "233": 138, "234": 138, "235": 138, "236": 138, "237": 138, "238": 140, "244": 121, "252": 121, "253": 122, "254": 123, "255": 124, "256": 124, "257": 124, "258": 124, "259": 124, "260": 124, "261": 124, "262": 125, "263": 126, "264": 126, "265": 126, "266": 126, "267": 126, "268": 126, "269": 126, "275": 107, "284": 107, "285": 108, "286": 109, "287": 109, "288": 109, "289": 110, "290": 111, "291": 112, "292": 113, "293": 113, "294": 113, "295": 113, "296": 113, "297": 115, "298": 116, "299": 116, "300": 116, "306": 163, "313": 163, "314": 164, "315": 165, "316": 166, "317": 166, "318": 166, "319": 166, "325": 319}, "source_encoding": "utf-8", "uri": "arusahni_helper.tmpl", "filename": "themes/zen/templates/arusahni_helper.tmpl"}
__M_END_METADATA
"""
