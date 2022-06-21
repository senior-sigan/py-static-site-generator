from ssg.backlinks import inject_internal_links
from ssg.models import Page


def test_find_links():
    page = Page(
        html='''
        <ul>
            <li><a href="/internal_link/">Internal 1</a></li>
            <li><a href="internal_link/test/">Internal 2</a></li>
            <li><a href="http://example.com">External</a></li>
            <li><a href="https://example.com">External</a></li>
            <li><a href="ftp://example.com">External</a></li>
            <li><a href="//example.com">External</a></li>
        </ul>
        ''',
    )
    inject_internal_links(page)
    assert "/internal_link/" in page['links']
    assert "internal_link/test/" in page['links']
    assert len(page['links']) == 2
