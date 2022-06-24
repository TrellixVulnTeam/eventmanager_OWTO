from django.urls import path, include

from .views import (
    EventListInternalView,
    EventListFilterInternalView,
    EventListView,
    EventMemberDetailView,
    EventUpdateCapacityView,
    FilteredEventListView,
    EventCreateView,
    EventLocationCreateView,
    EventLocationListView,
    EventLocationUpdateView,
    EventLocationReadView,
    EventLocationDeleteView,
    EventOrganizerCreateView,
    EventCategoryListView,
    EventCategoryCreateView,
    EventUpdateView,
    EventReadView,
    EventDetailView,
    EventDeleteView,
    EventMemberUpdateView,
    EventUpdateCapacityView,
    search_event,
    moodle,
    home,
    dashboard,
    event_add_member,
    get_moodle_data,
    EventApi,
    EventMembersListView,
    EventMemberDetailView,
    EventMemberDeleteView,
    EventMemberCreateView,
    export_members_csv,
    export_mv_members_csv,
    members_dashboard_view,
    export_ft_members_csv,
    export_ft_members_xls,
)

# sentry test
def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("sentry-debug/", trigger_error),  # sentry test
    path("tinymce/", include("tinymce.urls")),
    path("", home, name="home"),
    path("dashboard/", dashboard, name="dashboard"),
    path("event_list/", EventListView.as_view(), name="event-list"),
    path("event_filter/", FilteredEventListView.as_view(), name="event-filter"),
    path("event_create/", EventCreateView.as_view(), name="event-create"),
    path(
        "event_location/lost",
        EventLocationListView.as_view(),
        name="event-location-list",
    ),
    path(
        "event_location_create/",
        EventLocationCreateView.as_view(),
        name="event-location-create",
    ),
    path(
        "location_update/<int:pk>",
        EventLocationUpdateView.as_view(),
        name="location-update",
    ),
    path(
        "location_read/<int:pk>", EventLocationReadView.as_view(), name="location-read"
    ),
    path(
        "location_delete/<int:pk>",
        EventLocationDeleteView.as_view(),
        name="location-delete",
    ),
    path(
        "event_organizer_create/",
        EventOrganizerCreateView.as_view(),
        name="event-organizer-create",
    ),
    path(
        "event_create_nm/",
        EventCreateView.as_view(template_name="events/bootstrap/create_event_nm.html"),
        name="event-create-nm",
    ),  # no modal template
    path(
        "event_list_internal_filter/",
        EventListFilterInternalView.as_view(),
        name="event-list-internal-filter",
    ),
    path("event_update/<int:pk>", EventUpdateView.as_view(), name="event-update"),
    path("event_read/<int:pk>", EventReadView.as_view(), name="event-read"),
    path("event_delete/<int:pk>", EventDeleteView.as_view(), name="event-delete"),
    path(
        "event_list_internal/",
        EventListInternalView.as_view(),
        name="event-list-internal",
    ),
    path("category-list/", EventCategoryListView.as_view(), name="event-category-list"),
    path(
        "create-category/",
        EventCategoryCreateView.as_view(),
        name="create-event-category",
    ),
    path("detail/<slug:slug>", EventDetailView.as_view(), name="event-detail"),
    path(
        "event/<int:pk>/update_capacity/",
        EventUpdateCapacityView.as_view(),
        name="update-capacity",
    ),
    path("event_add_member/<slug:slug>", event_add_member, name="event-add-member"),
    path("search_event/", search_event, name="search-event"),
    path("moodle_list/", moodle, name="moodle-list"),
    path("get_moodle_data/", get_moodle_data, name="get-moodle-data"),
    path("events-api/", EventApi.as_view(), name="Event"),
    path("members/<event>/", EventMembersListView.as_view(), name="members"),
    path(
        "members/detail/<int:pk>/",
        EventMemberDetailView.as_view(),
        name="member-detail",
    ),
    path(
        "members/update/<int:pk>/",
        EventMemberUpdateView.as_view(),
        name="member-update",
    ),
    path(
        "members/delete/<int:pk>/",
        EventMemberDeleteView.as_view(),
        name="member-delete",
    ),
    path(
        "members/create/<event>", EventMemberCreateView.as_view(), name="member-create"
    ),
    path("members/export/csv/", export_members_csv, name="export-members-csv"),
    path("members_mv/export/csv/", export_mv_members_csv, name="export-members-mv-csv"),
    path("members_dashboard/", members_dashboard_view, name="members-dashboard"),
    path("members_ft/export/csv/", export_ft_members_csv, name="export-members-ft-csv"),
    path(
        "members_ft/export/excel/", export_ft_members_xls, name="export-members-ft-xls"
    ),
]
