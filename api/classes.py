from rest_framework import permissions
from rest_framework.metadata import BaseMetadata


class IsAuthenticatedAndReadOnly(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return super(IsAuthenticatedAndReadOnly, self).has_permission(
                request, view)


class APIRootMetadata(BaseMetadata):
    """
    Don't include field and other information for `OPTIONS` requests.
    Just return the name and description.
    """
    def determine_metadata(self, request, view):

        if view.get_view_name() == "Encrypt List":
            actions = {
                "GET": {
                    "read_only": False,
                    "parameters required": True,
                    "parameters": {
                        "given_name": "Please enter Given Name",
                        "surname": "Please enter Surname",
                        "key": "Please enter Encryption Key",
                    },
                },
            }
        elif view.get_view_name() == "Decrypt List":
            actions = {
                "GET": {
                    "read_only": True,
                    "parameters required": True,
                    "parameters": {
                        "given_name": "Please enter Encrypted Given Name",
                        "surname": "Please enter Encrypted Surname",
                        "key": "Please enter Encryption Key",
                    },
                },
            }
        elif view.get_view_name() == "Encrypt Base64 List":
            actions = {
                "GET": {
                    "read_only": True,
                    "parameters required": True,
                    "parameters": {
                        "given_name": "Please enter Given Name",
                        "surname": "Please enter Surname",
                    },
                },
            }
        elif view.get_view_name() == "Decrypt Base64 List":
            actions = {
                "GET": {
                    "read_only": True,
                    "parameters required": True,
                    "parameters": {
                        "given_name": "Please enter Base64 Given Name",
                        "surname": "Please enter Base64 Surname",
                    },
                },
            }
        else:
            actions = {}
        return {
            'name': view.get_view_name(),
            'description': view.get_view_description(),
            'renders': [renderer.media_type for renderer in
                        view.renderer_classes],
            'parses': [parser.media_type for parser in view.parser_classes],
            'actions': actions,
        }
