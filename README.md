# ckanext-mo-observations

A plugin for retrieving hourly weather observation data from the Met Office.

## Components

### Feed retrieval

There is a paster command that can be run frequently (say every 6 hours) that
will determine which feeds are available before fetching them and storing them
in the database.

