# Django CMS Basic Boilerplate

This is a basic boilerplate to build Django CMS applications; the folder structure tries to be as simple and clear as possible.

## Boilerplate key points

- It is intended to be published on Google Cloud Run trought gunicorn.
- It uses Google Cloud Storage as production media and static files' repository.
- The docker image is based on python:3.7-buster.
- Settings modules are separated on two python files, one for development and one for production.
- It inculdes djangocms_svimage and djangocms_cssimport plugins.
- It encourages the use of piper-cli to synchronize snippets between the local development environment and the portal database.
