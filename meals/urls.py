from django.urls import path
from .views import (
    DistanceView, 
    HotelRestaurantAdminMealListCreateView, 
    HotelRestaurantAdminMealGetUpdateDeleteView,
    MealCategoryListCreateView,
    MealCategoryRetrieveUpdateDestroyView,
    SubCategoryListCreateView,
    SubCategoryRetrieveUpdateDestroyView,
    MealListCreateView,
    MealRetrieveUpdateDestroyView,
    MealListByUsernameView,
    QrListByUsernameView,
    QrRetrieveBySlugView,
    QrSubCategoryListView,
    HotelRestaurantAdminCategoryListByUsernameView,
    HotelRestaurantAdminCategoryRetriveUpdateDestroyByUsernameView,
    HotelRestaurantAdminSubCategoryListByUsernameView,
    HotelRestaurantAdminSubCategoryRetrieveUpdateDestroyView,
    MealImageUpdateView,
    MealImageCreateView,
    MealImageDeleteView,
    MealVideoUpdateDeleteView,
    MealSizeDeleteView,
    MealSizeUpdateView,
    MealSearchView,
    RestaurantSocialMediaGetView,
    RestaurantSocialMediaUpdateView,
    RestaurantSocialMediaReviewRetrieveView,
    RestaurantSocialMediaReviewUpdateView,
    BasketItemCreateView,
    BasketItemDeleteView,
    BasketItemUpdateView,
    BasketGetView,
    OrderCreateView,
    OrderGetView,
    OrderListView

)

urlpatterns = [
    path('distance/', DistanceView.as_view(), name='distance-view'),
    path('hotel-restaurant-admin/meal/list-create/<str:restaurant_username>', HotelRestaurantAdminMealListCreateView.as_view(), name='hotel_admin_meal_list'),
    path('hotel-restaurant-admin/meal/size/update/<int:size_id>', MealSizeUpdateView.as_view()),
    path('hotel-restaurant-admin/meal/size/delete/<int:size_id>', MealSizeDeleteView.as_view()),
    path('hotel-restaurant-admin/meal/<str:meal_slug>', HotelRestaurantAdminMealGetUpdateDeleteView.as_view(), name='hotel_admin_meal_get_update_delete'),
    path('hotel-restaurant-admin/mealcategory/<str:username>', HotelRestaurantAdminCategoryListByUsernameView.as_view(), name='hotel_admin_mealcategory_list_create'),
    path('hotel-restaurant-admin/mealcategory/<str:slug>/', HotelRestaurantAdminCategoryRetriveUpdateDestroyByUsernameView.as_view(), name='hotel_admin_mealcategory_retrieve_update_delete'),
    path('hotel-restaurant-admin/subcategory/<str:username>', HotelRestaurantAdminSubCategoryListByUsernameView.as_view(), name='hotel_admin_subcategory_list_create'),
    path('hotel-restaurant-admin/subcategory/<str:slug>/', HotelRestaurantAdminSubCategoryRetrieveUpdateDestroyView.as_view(), name='hotel_admin_subcategory_retrieve_update_destroy'),
    path('hotel-restaurant-admin/meal/image/update/<int:image_id>', MealImageUpdateView.as_view()),
    path('hotel-restaurant-admin/meal/image/create', MealImageCreateView.as_view()),
    path('hotel-restaurant-admin/meal/image/delete/<int:image_id>', MealImageDeleteView.as_view()),
    path('hotel-restaurant-admin/meal/video/delete-update/<slug:meal_slug>', MealVideoUpdateDeleteView.as_view()),
    path('meal-category/<str:lang>', MealCategoryListCreateView.as_view(), name='mealcategory_list_create'),
    path('meal-category/<str:lang>/<str:slug>', MealCategoryRetrieveUpdateDestroyView.as_view(), name='mealcategory_get_update_delete'),
    path('sub-category/<str:lang>', SubCategoryListCreateView.as_view(), name='sub-category_list_create'),
    path('sub-category/<str:lang>/<str:slug>', SubCategoryRetrieveUpdateDestroyView.as_view(), name='sub-category_get_update_delete'),
    path('meal-admin/<str:lang>', MealListCreateView.as_view(), name='meal_list_create'),
    path('meal-admin/<str:slug>', MealRetrieveUpdateDestroyView.as_view(), name='meal_get_update_delete'),
    path('meal-admin/search/<str:username>', MealListByUsernameView.as_view(), name='meal_list_username_create'),
    path('qr-client/list/<str:lang>/<str:username>', QrListByUsernameView.as_view(), name='qr_list_username_create'),
    path('qr-client/search/<str:lang>/<str:username>/<str:name>', MealSearchView.as_view()),
    path('qr-client/retrieve/<str:lang>/<str:slug>', QrRetrieveBySlugView.as_view(), name='qr_retrieve_username_create'),
    path('qr-client/subcategory-list/<str:lang>/<str:username>/<str:slug>', QrSubCategoryListView.as_view(), name='qr_subcategory_list'),
    path('restaurant-admin/social-media/get/<str:lang>', RestaurantSocialMediaGetView.as_view(), name='restaurant_social_media_get'),
    path('restaurant-admin/social-media/update/<str:lang>', RestaurantSocialMediaUpdateView.as_view(), name='restaurant_social_media_update'),
    path('restaurant-admin/social-media/review/get/<str:lang>', RestaurantSocialMediaReviewRetrieveView.as_view(), name='restaurant_social_media_review'),
    path('restaurant-admin/social-media/review/update/<str:lang>', RestaurantSocialMediaReviewUpdateView.as_view(), name='restaurant_social_media_review_update'),

    path('basket/item/create', BasketItemCreateView.as_view(), name='basket_item_create'),
    path('basket/item/delete/<int:id>', BasketItemDeleteView.as_view(), name='basket_item_delete'),
    path('basket/item/update/<int:id>', BasketItemUpdateView.as_view(), name='basket_item_update'),
    path('basket/get', BasketGetView.as_view(), name='basket_get'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/get', OrderGetView.as_view(), name='order_get'),
    path('order/list', OrderListView.as_view(), name='order_list'),
]
