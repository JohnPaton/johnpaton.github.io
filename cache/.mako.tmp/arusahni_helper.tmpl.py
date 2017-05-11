# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1494531910.2115512
_enable_loop = True
_template_filename = 'themes/zen/templates/arusahni_helper.tmpl'
_template_uri = 'arusahni_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_tags', 'html_sourcelink', 'late_load_js', 'html_title', 'html_feedlinks', 'html_stylesheets', 'html_translations', 'html_headstart', 'html_navigation_links']


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


def render_html_tags(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        messages = context.get('messages', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
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


def render_html_sourcelink(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        show_sourcelink = context.get('show_sourcelink', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
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
        use_cdn = context.get('use_cdn', UNDEFINED)
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
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
        title = context.get('title', UNDEFINED)
        post = context.get('post', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <h1 class="p-name entry-title" itemprop="headline name">')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('</h1>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        rss_link = context.get('rss_link', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        post = context.get('post', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        notes = context.get('notes', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        annotations = context.get('annotations', UNDEFINED)
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


def render_html_translations(context,post):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        favicons = context.get('favicons', UNDEFINED)
        striphtml = context.get('striphtml', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        def html_stylesheets():
            return render_html_stylesheets(context)
        use_cdn = context.get('use_cdn', UNDEFINED)
        title = context.get('title', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
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
        lang = context.get('lang', UNDEFINED)
        navigation_links = context.get('navigation_links', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "uri": "arusahni_helper.tmpl", "filename": "themes/zen/templates/arusahni_helper.tmpl", "line_map": {"16": 0, "21": 57, "22": 85, "23": 105, "24": 119, "25": 129, "26": 143, "27": 150, "28": 161, "29": 168, "35": 132, "41": 132, "42": 133, "43": 134, "44": 136, "45": 136, "46": 137, "47": 138, "48": 138, "49": 138, "50": 138, "51": 138, "52": 140, "58": 163, "65": 163, "66": 164, "67": 165, "68": 166, "69": 166, "70": 166, "71": 166, "77": 87, "84": 87, "85": 88, "86": 89, "87": 90, "88": 92, "89": 93, "90": 95, "91": 96, "92": 97, "93": 99, "94": 100, "95": 104, "96": 104, "97": 104, "103": 146, "109": 146, "110": 147, "111": 148, "112": 148, "113": 148, "119": 107, "128": 107, "129": 108, "130": 109, "131": 109, "132": 109, "133": 110, "134": 111, "135": 112, "136": 113, "137": 113, "138": 113, "139": 113, "140": 113, "141": 115, "142": 116, "143": 116, "144": 116, "150": 59, "160": 59, "161": 60, "162": 61, "163": 62, "164": 64, "165": 65, "166": 67, "167": 68, "168": 69, "169": 70, "170": 71, "171": 73, "172": 76, "173": 77, "174": 80, "175": 81, "176": 81, "177": 81, "178": 82, "179": 83, "180": 83, "181": 83, "187": 152, "195": 152, "196": 153, "197": 154, "198": 155, "199": 156, "200": 156, "201": 156, "202": 156, "203": 156, "204": 157, "205": 157, "211": 3, "234": 3, "235": 7, "236": 8, "237": 9, "238": 10, "239": 12, "240": 13, "241": 15, "242": 16, "243": 18, "244": 21, "245": 22, "246": 25, "247": 25, "248": 25, "249": 28, "250": 29, "251": 29, "252": 29, "253": 31, "254": 32, "255": 32, "256": 32, "257": 32, "258": 34, "259": 34, "260": 35, "261": 35, "262": 36, "263": 37, "264": 37, "265": 37, "266": 39, "267": 40, "268": 41, "269": 42, "270": 42, "271": 42, "272": 42, "273": 42, "274": 42, "275": 42, "276": 45, "277": 46, "278": 47, "279": 47, "280": 47, "281": 49, "282": 50, "283": 51, "284": 52, "285": 53, "286": 55, "287": 56, "288": 56, "294": 121, "302": 121, "303": 122, "304": 123, "305": 124, "306": 124, "307": 124, "308": 124, "309": 124, "310": 124, "311": 124, "312": 125, "313": 126, "314": 126, "315": 126, "316": 126, "317": 126, "318": 126, "319": 126, "325": 319}}
__M_END_METADATA
"""
