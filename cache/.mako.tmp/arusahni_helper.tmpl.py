# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496046951.5141773
_enable_loop = True
_template_filename = 'themes/zen/templates/arusahni_helper.tmpl'
_template_uri = 'arusahni_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_feedlinks', 'html_title', 'html_translations', 'html_sourcelink', 'late_load_js', 'html_tags', 'html_headstart', 'html_navigation_links', 'html_stylesheets']


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


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        _link = context.get('_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
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
        len = context.get('len', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        description = context.get('description', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        striphtml = context.get('striphtml', UNDEFINED)
        title = context.get('title', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
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


def render_html_navigation_links(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rel_link = context.get('rel_link', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        notes = context.get('notes', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
        post = context.get('post', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"16": 0, "21": 57, "22": 85, "23": 105, "24": 119, "25": 129, "26": 143, "27": 150, "28": 161, "29": 168, "35": 107, "44": 107, "45": 108, "46": 109, "47": 109, "48": 109, "49": 110, "50": 111, "51": 112, "52": 113, "53": 113, "54": 113, "55": 113, "56": 113, "57": 115, "58": 116, "59": 116, "60": 116, "66": 146, "72": 146, "73": 147, "74": 148, "75": 148, "76": 148, "82": 152, "90": 152, "91": 153, "92": 154, "93": 155, "94": 156, "95": 156, "96": 156, "97": 156, "98": 156, "99": 157, "100": 157, "106": 163, "113": 163, "114": 164, "115": 165, "116": 166, "117": 166, "118": 166, "119": 166, "125": 87, "132": 87, "133": 88, "134": 89, "135": 90, "136": 92, "137": 93, "138": 95, "139": 96, "140": 97, "141": 99, "142": 100, "143": 104, "144": 104, "145": 104, "151": 132, "157": 132, "158": 133, "159": 134, "160": 136, "161": 136, "162": 137, "163": 138, "164": 138, "165": 138, "166": 138, "167": 138, "168": 140, "174": 3, "197": 3, "198": 7, "199": 8, "200": 9, "201": 10, "202": 12, "203": 13, "204": 15, "205": 16, "206": 18, "207": 21, "208": 22, "209": 25, "210": 25, "211": 25, "212": 28, "213": 29, "214": 29, "215": 29, "216": 31, "217": 32, "218": 32, "219": 32, "220": 32, "221": 34, "222": 34, "223": 35, "224": 35, "225": 36, "226": 37, "227": 37, "228": 37, "229": 39, "230": 40, "231": 41, "232": 42, "233": 42, "234": 42, "235": 42, "236": 42, "237": 42, "238": 42, "239": 45, "240": 46, "241": 47, "242": 47, "243": 47, "244": 49, "245": 50, "246": 51, "247": 52, "248": 53, "249": 55, "250": 56, "251": 56, "257": 121, "265": 121, "266": 122, "267": 123, "268": 124, "269": 124, "270": 124, "271": 124, "272": 124, "273": 124, "274": 124, "275": 125, "276": 126, "277": 126, "278": 126, "279": 126, "280": 126, "281": 126, "282": 126, "288": 59, "298": 59, "299": 60, "300": 61, "301": 62, "302": 64, "303": 65, "304": 67, "305": 68, "306": 69, "307": 70, "308": 71, "309": 73, "310": 76, "311": 77, "312": 80, "313": 81, "314": 81, "315": 81, "316": 82, "317": 83, "318": 83, "319": 83, "325": 319}, "uri": "arusahni_helper.tmpl", "filename": "themes/zen/templates/arusahni_helper.tmpl"}
__M_END_METADATA
"""
