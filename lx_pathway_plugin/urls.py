"""
Studio URL configuration for lx-pathway-plugin.
"""
from django.urls import include, re_path

from . import views

urlpatterns = [
    re_path(r'^api/lx-pathways/v1/', include([
        re_path(r'pathway/$', views.create_pathway),
        # Get/edit/delete a specific pathway:
        re_path(r'pathway/(?P<pathway_key_str>[^/]+)/$', views.PathwayView.as_view()),
        # Publish or revert changes to a pathway:
        re_path(r'pathway/(?P<pathway_key_str>[^/]+)/publish/$', views.PathwayPublishView.as_view()),
    ])),
]
