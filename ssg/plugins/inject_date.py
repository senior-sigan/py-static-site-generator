from datetime import datetime


def apply(site, page) -> None:
    date = page.get('metadata', {}).get('date')
    if date is None:
        return None
    date_format = page['metadata'].get('date_format', site['date_format'])
    page['date'] = datetime.strptime(date, date_format)
