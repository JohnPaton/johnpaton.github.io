# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1487709126.951241
_enable_loop = True
_template_filename = 'c:/users/john paton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_translations', 'late_load_js', 'html_stylesheets', 'html_headstart', 'html_feedlinks']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n\n')
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        abs_link = context.get('abs_link', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <ul class="translations">\n')
        for langname in sorted(translations):
            if langname != lang:
                __M_writer('            <li><a href="')
                __M_writer(str(abs_link(_link("root", None, langname))))
                __M_writer('" rel="alternate" hreflang="')
                __M_writer(str(langname))
                __M_writer('">')
                __M_writer(str(messages("LANGUAGE", langname)))
                __M_writer('</a></li>\n')
        __M_writer('    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_late_load_js(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        social_buttons_code = context.get('social_buttons_code', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(social_buttons_code))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
        use_bundles = context.get('use_bundles', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if use_bundles:
            if use_cdn:
                __M_writer('            <link href="/assets/css/all.css" rel="stylesheet" type="text/css">\n')
            else:
                __M_writer('            <link href="/assets/css/all-nocdn.css" rel="stylesheet" type="text/css">\n')
        else:
            __M_writer('        <link href="/assets/css/rst.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/code.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/theme.css" rel="stylesheet" type="text/css">\n')
            if has_custom_css:
                __M_writer('            <link href="/assets/css/custom.css" rel="stylesheet" type="text/css">\n')
        if needs_ipython_css:
            __M_writer('        <link href="/assets/css/ipython.min.css" rel="stylesheet" type="text/css">\n        <link href="/assets/css/nikola_ipython.css" rel="stylesheet" type="text/css">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        def html_stylesheets():
            return render_html_stylesheets(context)
        theme_color = context.get('theme_color', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        title = context.get('title', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        abs_link = context.get('abs_link', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        blog_title = context.get('blog_title', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        description = context.get('description', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html ')
        __M_writer("prefix='")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('og: http://ogp.me/ns# article: http://ogp.me/ns/article# ')
        if comment_system == 'facebook':
            __M_writer('fb: http://ogp.me/ns/fb#\n')
        __M_writer("' ")
        if use_open_graph or (twitter_card and twitter_card['use_twitter_cards']):
            __M_writer('vocab="http://ogp.me/ns" ')
        if is_rtl:
            __M_writer('dir="rtl" ')
        __M_writer('lang="')
        __M_writer(str(lang))
        __M_writer('">\n<head>\n    <meta charset="utf-8">\n')
        if use_base_tag:
            __M_writer('    <base href="')
            __M_writer(str(abs_link(permalink)))
            __M_writer('">\n')
        if description:
            __M_writer('    <meta name="description" content="')
            __M_writer(filters.html_escape(str(description)))
            __M_writer('">\n')
        __M_writer('    <meta name="viewport" content="width=device-width">\n')
        if title == blog_title:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        else:
            __M_writer('        <title>')
            __M_writer(filters.html_escape(str(title)))
            __M_writer(' | ')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</title>\n')
        __M_writer('\n    ')
        __M_writer(str(html_stylesheets()))
        __M_writer('\n    <meta name="theme-color" content="')
        __M_writer(str(theme_color))
        __M_writer('">\n    <meta name="generator" content="Nikola (getnikola.com)">\n    ')
        __M_writer(str(html_feedlinks()))
        __M_writer('\n    <link rel="canonical" href="')
        __M_writer(str(abs_link(permalink)))
        __M_writer('">\n\n')
        if favicons:
            for name, file, size in favicons:
                __M_writer('            <link rel="')
                __M_writer(str(name))
                __M_writer('" href="')
                __M_writer(str(file))
                __M_writer('" sizes="')
                __M_writer(str(size))
                __M_writer('"/>\n')
        __M_writer('\n')
        if comment_system == 'facebook':
            __M_writer('        <meta property="fb:app_id" content="')
            __M_writer(str(comment_system_id))
            __M_writer('">\n')
        __M_writer('\n')
        if prevlink:
            __M_writer('        <link rel="prev" href="')
            __M_writer(str(prevlink))
            __M_writer('" type="text/html">\n')
        if nextlink:
            __M_writer('        <link rel="next" href="')
            __M_writer(str(nextlink))
            __M_writer('" type="text/html">\n')
        __M_writer('\n    ')
        __M_writer(str(mathjax_config))
        __M_writer('\n')
        if use_cdn:
            __M_writer('        <!--[if lt IE 9]><script src="https://html5shim.googlecode.com/svn/trunk/html5.js"></script><![endif]-->\n')
        else:
            __M_writer('        <!--[if lt IE 9]><script src="')
            __M_writer(str(url_replacer(permalink, '/assets/js/html5.js', lang, url_type)))
            __M_writer('"></script><![endif]-->\n')
        __M_writer('\n    ')
        __M_writer(str(extra_head_data))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        len = context.get('len', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if rss_link:
            __M_writer('        ')
            __M_writer(str(rss_link))
            __M_writer('\n')
        elif generate_rss:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/rss+xml" title="RSS (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('rss', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/rss+xml" title="RSS" href="')
                __M_writer(str(_link('rss', None)))
                __M_writer('">\n')
        if generate_atom:
            if len(translations) > 1:
                for language in sorted(translations):
                    __M_writer('                <link rel="alternate" type="application/atom+xml" title="Atom (')
                    __M_writer(str(language))
                    __M_writer(')" href="')
                    __M_writer(str(_link('index_atom', None, language)))
                    __M_writer('">\n')
            else:
                __M_writer('            <link rel="alternate" type="application/atom+xml" title="Atom" href="')
                __M_writer(str(_link('index_atom', None)))
                __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "base_helper.tmpl", "filename": "c:/users/john paton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl", "line_map": {"16": 0, "21": 2, "22": 68, "23": 72, "24": 93, "25": 116, "26": 126, "32": 118, "42": 118, "43": 120, "44": 121, "45": 122, "46": 122, "47": 122, "48": 122, "49": 122, "50": 122, "51": 122, "52": 125, "58": 70, "63": 70, "64": 71, "65": 71, "71": 74, "79": 74, "80": 75, "81": 76, "82": 77, "83": 78, "84": 79, "85": 81, "86": 82, "87": 85, "88": 86, "89": 89, "90": 90, "96": 3, "125": 3, "126": 6, "127": 7, "128": 8, "129": 10, "130": 11, "131": 13, "132": 14, "133": 15, "134": 17, "135": 18, "136": 21, "137": 21, "138": 21, "139": 24, "140": 25, "141": 25, "142": 25, "143": 27, "144": 28, "145": 28, "146": 28, "147": 30, "148": 31, "149": 32, "150": 32, "151": 32, "152": 33, "153": 34, "154": 34, "155": 34, "156": 34, "157": 34, "158": 36, "159": 37, "160": 37, "161": 38, "162": 38, "163": 40, "164": 40, "165": 41, "166": 41, "167": 43, "168": 44, "169": 45, "170": 45, "171": 45, "172": 45, "173": 45, "174": 45, "175": 45, "176": 48, "177": 49, "178": 50, "179": 50, "180": 50, "181": 52, "182": 53, "183": 54, "184": 54, "185": 54, "186": 56, "187": 57, "188": 57, "189": 57, "190": 59, "191": 60, "192": 60, "193": 61, "194": 62, "195": 63, "196": 64, "197": 64, "198": 64, "199": 66, "200": 67, "201": 67, "207": 95, "218": 95, "219": 96, "220": 97, "221": 97, "222": 97, "223": 98, "224": 99, "225": 100, "226": 101, "227": 101, "228": 101, "229": 101, "230": 101, "231": 103, "232": 104, "233": 104, "234": 104, "235": 107, "236": 108, "237": 109, "238": 110, "239": 110, "240": 110, "241": 110, "242": 110, "243": 112, "244": 113, "245": 113, "246": 113, "252": 246}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
