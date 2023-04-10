BASE_URL = "https://www.booking.com/"


class SortChoice:
    POPULARITY = 'popularity'
    HOME_AND_APARTMENT_FIRST = 'upsort_bh'
    LOWEST_PRICE = 'price'
    BEST_REVIEW_AND_LOWEST_PRICE = "review_score_and_price"
    RATING_HIGH_TO_LOW = "class"
    RATING_LOW_TO_HIGH = "class_asc"
    RATING_AND_PRICE = "class_and_price"
    DISTANCE_FROM_CITY_CENTRE = "distance_from_search"
    TOP_REVIEWED = "bayesian_review_score"
