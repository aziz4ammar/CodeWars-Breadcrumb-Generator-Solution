def generate_bc(url, separator):
    if '//' in url:
        url = url[url.index('//') + 2:]

    url = url.rstrip('/')

    try:
        for i, c in enumerate(url):
            if c in ['?', '#']:
                url = url[0:i]
                break

        menus = url.split('/')[1:]
        if menus and 'index.' == menus[-1][0:6]:
            menus = menus[:-1]
        if not menus:
            return '<span class="active">HOME</span>'

        breadcrumb = '<a href="/">HOME</a>'

        for i, e in enumerate(menus[:-1]):
            breadcrumb += separator + '<a href="/{}/">{}</a>'.format('/'.join(menus[:i + 1]), get_element_name(e))

        breadcrumb += separator + '<span class="active">{}</span>'.format(get_element_name(menus[-1]))
        return breadcrumb
    except:
        return url


ignore_words = ["the", "of", "in", "from", "by", "with", "and", "or", "for", "to", "at", "a"]


def get_element_name(element):
    acronyms = element.split('-')
    for i, c in enumerate(acronyms[-1]):
        if c == '.':
            acronyms[-1] = acronyms[-1][:i]
            break

    if len(element) > 30:
        for i, c in reversed(list(enumerate(acronyms))):
            if c in ignore_words:
                acronyms.pop(i)
        return ''.join([s[0].upper() for s in acronyms])

    return ' '.join([s.upper() for s in acronyms])



assert generate_bc("mysite.com/pictures/holidays.html",
                   " : ") == '<a href="/">HOME</a> : <a href="/pictures/">PICTURES</a> : <span class="active">HOLIDAYS</span>'
assert generate_bc("www.codewars.com/users/GiacomoSorbi?ref=CodeWars",
                   " / ") == '<a href="/">HOME</a> / <a href="/users/">USERS</a> / <span class="active">GIACOMOSORBI</span>'
assert generate_bc("www.microsoft.com/important/confidential/docs/index.htm#top",
                   " * ") == '<a href="/">HOME</a> * <a href="/important/">IMPORTANT</a> * <a href="/important/confidential/">CONFIDENTIAL</a> * <span class="active">DOCS</span>'
assert generate_bc("mysite.com/very-long-url-to-make-a-silly-yet-meaningful-example/example.asp",
                   " > ") == '<a href="/">HOME</a> > <a href="/very-long-url-to-make-a-silly-yet-meaningful-example/">VLUMSYME</a> > <span class="active">EXAMPLE</span>'
assert generate_bc("www.very-long-site_name-to-make-a-silly-yet-meaningful-example.com/users/giacomo-sorbi",
                   " + ") == '<a href="/">HOME</a> + <a href="/users/">USERS</a> + <span class="active">GIACOMO SORBI</span>'

# print("https://www.linkedin.com/in/giacomosorbi".index('//'))
# print(generate_bc("https://www.linkedin.com/in/giacomosorbi", " * "))
assert generate_bc("https://www.linkedin.com/in/giacomosorbi",
                   " * ") == '<a href="/">HOME</a> * <a href="/in/">IN</a> * <span class="active">GIACOMOSORBI</span>'
print(generate_bc("www.agcpartners.co.uk", " * "))
assert generate_bc("www.agcpartners.co.uk", " * ") == '<span class="active">HOME</span>'
assert generate_bc("www.agcpartners.co.uk/", " * ") == '<span class="active">HOME</span>'
assert generate_bc("www.agcpartners.co.uk/index.html", " * ") == '<span class="active">HOME</span>'
assert generate_bc("www.google.ca/index.php", " * ") == '<span class="active">HOME</span>'