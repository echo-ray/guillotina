from guillotina import routes
from guillotina.response import InvalidRoute

import pytest


def test_convert_simple_route_to_view_name():
    assert routes.Route('@foobar').view_name == '@foobar'


def test_convert_non_routing_to_view_name():
    assert routes.Route('foo/bar').view_name == 'foo/bar'


def test_convert_route_to_view_name():
    assert routes.Route('@foobar/{foo}/{bar}').view_name == '@foobar//'


def test_invalid_non_route():
    with pytest.raises(InvalidRoute):
        routes.Route('foobar/{foo}/{bar}')


def test_throws_error_for_invalid_route():
    with pytest.raises(InvalidRoute):
        routes.Route('@foobar/foobar/{foo}/{bar}')


def test_convert_path_to_view_name():
    assert routes.path_to_view_name('@foobar/foo/bar') == '@foobar//'


def test_convert_non_route_path_to_view_name():
    assert routes.path_to_view_name('foobar/foo/bar') == 'foobar/foo/bar'
