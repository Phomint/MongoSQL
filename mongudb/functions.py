def greater(object):
    return {'$gt': object}


def greater_equal(object):
    return {'$gte': object}


def isin(object):
    return {'$in': object}


def lower(object):
    return {'$lt': object}


def lower_equal(object):
    return {'$lt': object}