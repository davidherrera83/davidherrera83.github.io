def test_title(website):
    assert website.should().contain_title('David Herrera')

def test_header_display(website):
    assert website.get('h1 strong').should().have_text('David Herrera')

def test_avatar_image(website):
    assert website.get('img[src="images/avatar_color.png"]').should().be_visible()

def test_main_content_sections(website):
    assert website.contains('Recent Work')
    assert website.contains('Get In Touch')

def test_external_links(website):
    assert website.get('a[href="https://www.hudl.com/"]').should().exist()

