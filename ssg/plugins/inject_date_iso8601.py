def apply(site, page) -> None:
    # 2013-05-16T08:36:00+00:00
    date = page.get('date')
    if date is not None:
        page['date_iso8601'] = date.isoformat()
