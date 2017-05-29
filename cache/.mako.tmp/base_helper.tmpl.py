# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1496046522.2139919
_enable_loop = True
_template_filename = 'c:/users/johnpaton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl'
_template_uri = 'base_helper.tmpl'
_source_encoding = 'utf-8'
_exports = ['html_headstart', 'html_stylesheets', 'late_load_js', 'html_feedlinks', 'html_translations']


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


def render_html_headstart(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        def html_stylesheets():
            return render_html_stylesheets(context)
        blog_title = context.get('blog_title', UNDEFINED)
        nextlink = context.get('nextlink', UNDEFINED)
        url_replacer = context.get('url_replacer', UNDEFINED)
        title = context.get('title', UNDEFINED)
        favicons = context.get('favicons', UNDEFINED)
        extra_head_data = context.get('extra_head_data', UNDEFINED)
        url_type = context.get('url_type', UNDEFINED)
        theme_color = context.get('theme_color', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        twitter_card = context.get('twitter_card', UNDEFINED)
        comment_system = context.get('comment_system', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        description = context.get('description', UNDEFINED)
        def html_feedlinks():
            return render_html_feedlinks(context)
        prevlink = context.get('prevlink', UNDEFINED)
        is_rtl = context.get('is_rtl', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        use_open_graph = context.get('use_open_graph', UNDEFINED)
        use_base_tag = context.get('use_base_tag', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        comment_system_id = context.get('comment_system_id', UNDEFINED)
        mathjax_config = context.get('mathjax_config', UNDEFINED)
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


def render_html_stylesheets(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        use_bundles = context.get('use_bundles', UNDEFINED)
        use_cdn = context.get('use_cdn', UNDEFINED)
        needs_ipython_css = context.get('needs_ipython_css', UNDEFINED)
        has_custom_css = context.get('has_custom_css', UNDEFINED)
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


def render_html_feedlinks(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        rss_link = context.get('rss_link', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        generate_atom = context.get('generate_atom', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        len = context.get('len', UNDEFINED)
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


def render_html_translations(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        translations = context.get('translations', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        lang = context.get('lang', UNDEFINED)
        abs_link = context.get('abs_link', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
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


"""
__M_BEGIN_METADATA
{"line_map": {"16": 0, "21": 2, "22": 68, "23": 72, "24": 93, "25": 116, "26": 126, "32": 3, "61": 3, "62": 6, "63": 7, "64": 8, "65": 10, "66": 11, "67": 13, "68": 14, "69": 15, "70": 17, "71": 18, "72": 21, "73": 21, "74": 21, "75": 24, "76": 25, "77": 25, "78": 25, "79": 27, "80": 28, "81": 28, "82": 28, "83": 30, "84": 31, "85": 32, "86": 32, "87": 32, "88": 33, "89": 34, "90": 34, "91": 34, "92": 34, "93": 34, "94": 36, "95": 37, "96": 37, "97": 38, "98": 38, "99": 40, "100": 40, "101": 41, "102": 41, "103": 43, "104": 44, "105": 45, "106": 45, "107": 45, "108": 45, "109": 45, "110": 45, "111": 45, "112": 48, "113": 49, "114": 50, "115": 50, "116": 50, "117": 52, "118": 53, "119": 54, "120": 54, "121": 54, "122": 56, "123": 57, "124": 57, "125": 57, "126": 59, "127": 60, "128": 60, "129": 61, "130": 62, "131": 63, "132": 64, "133": 64, "134": 64, "135": 66, "136": 67, "137": 67, "143": 74, "151": 74, "152": 75, "153": 76, "154": 77, "155": 78, "156": 79, "157": 81, "158": 82, "159": 85, "160": 86, "161": 89, "162": 90, "168": 70, "173": 70, "174": 71, "175": 71, "181": 95, "192": 95, "193": 96, "194": 97, "195": 97, "196": 97, "197": 98, "198": 99, "199": 100, "200": 101, "201": 101, "202": 101, "203": 101, "204": 101, "205": 103, "206": 104, "207": 104, "208": 104, "209": 107, "210": 108, "211": 109, "212": 110, "213": 110, "214": 110, "215": 110, "216": 110, "217": 112, "218": 113, "219": 113, "220": 113, "226": 118, "236": 118, "237": 120, "238": 121, "239": 122, "240": 122, "241": 122, "242": 122, "243": 122, "244": 122, "245": 122, "246": 125, "252": 246}, "source_encoding": "utf-8", "uri": "base_helper.tmpl", "filename": "c:/users/johnpaton/appdata/local/programs/python/python35-32/lib/site-packages/nikola/data/themes/base/templates/base_helper.tmpl"}
__M_END_METADATA
"""
