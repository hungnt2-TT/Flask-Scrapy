

def paginate_data(data, page, limit, total_count):
    paginated_data = {
        'data': data,
        'page': page,
        'limit': limit,
        'has_next': page < total_count // limit,
        'has_prev': page > 1,
        'result': len(data)
    }

    status = 1
    message = 'Success'

    response = {
        'status': status,
        'message': message,
        'data': paginated_data
    }

    return response


def get_page_limit(request):
    try:
        page = int(request.args.get('page'))
        limit = int(request.args.get('limit'))
        return page, limit
    except (ValueError, TypeError):
        raise ValueError('Invalid page or limit value.')
