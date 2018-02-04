test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(imdb_sorted) == tables.Table
          True
          >>> list(imdb_sorted.column('Title').take(range(4)))
          ['The Shawshank Redemption', 'The Godfather', 'The Godfather: Part II', 'Pulp Fiction']
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
