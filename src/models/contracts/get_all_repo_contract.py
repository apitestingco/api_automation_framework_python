get_all_repos = {
    "$schema": "http://json-schema.org/draft-07/schema",
    "$id": "http://example.com/example.json",
    "type": "array",
    "title": "The root schema",
    "description": "The root schema comprises the entire JSON document.",
    "default": [],
    "examples": [],
    "additionalItems": True,
    "items": {
        "anyOf": [
            {
                "$id": "#/items/anyOf/0",
                "type": "object",
                "title": "The first anyOf schema",
                "description": "An explanation about the purpose of this instance.",
                "default": {},
                "examples": [],
                "required": [
                    "id",
                    "node_id",
                    "name",
                    "full_name",
                    "private",
                    "owner",
                    "html_url",
                    "description",
                    "fork",
                    "url",
                    "forks_url",
                    "keys_url",
                    "collaborators_url",
                    "teams_url",
                    "hooks_url",
                    "issue_events_url",
                    "events_url",
                    "assignees_url",
                    "branches_url",
                    "tags_url",
                    "blobs_url",
                    "git_tags_url",
                    "git_refs_url",
                    "trees_url",
                    "statuses_url",
                    "languages_url",
                    "stargazers_url",
                    "contributors_url",
                    "subscribers_url",
                    "subscription_url",
                    "commits_url",
                    "git_commits_url",
                    "comments_url",
                    "issue_comment_url",
                    "contents_url",
                    "compare_url",
                    "merges_url",
                    "archive_url",
                    "downloads_url",
                    "issues_url",
                    "pulls_url",
                    "milestones_url",
                    "notifications_url",
                    "labels_url",
                    "releases_url",
                    "deployments_url",
                    "created_at",
                    "updated_at",
                    "pushed_at",
                    "git_url",
                    "ssh_url",
                    "clone_url",
                    "svn_url",
                    "homepage",
                    "size",
                    "stargazers_count",
                    "watchers_count",
                    "language",
                    "has_issues",
                    "has_projects",
                    "has_downloads",
                    "has_wiki",
                    "has_pages",
                    "forks_count",
                    "mirror_url",
                    "archived",
                    "disabled",
                    "open_issues_count",
                    "license",
                    "forks",
                    "open_issues",
                    "watchers",
                    "default_branch",
                    "permissions"
                ],
                "additionalProperties": True,
                "minProperties"  : 73,
                "properties": {
                    "id": {
                        "$id": "#/items/anyOf/0/properties/id",
                        "type": "integer",
                        "title": "The id schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            259075981
                        ]
                    },
                    "node_id": {
                        "$id": "#/items/anyOf/0/properties/node_id",
                        "type": "string",
                        "title": "The node_id schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "MDEwOlJlcG9zaXRvcnkyNTkwNzU5ODE="
                        ]
                    },
                    "name": {
                        "$id": "#/items/anyOf/0/properties/name",
                        "type": "string",
                        "title": "The name schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "helloapi"
                        ]
                    },
                    "full_name": {
                        "$id": "#/items/anyOf/0/properties/full_name",
                        "type": "string",
                        "title": "The full_name schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "apitestingco/helloapi"
                        ]
                    },
                    "private": {
                        "$id": "#/items/anyOf/0/properties/private",
                        "type": "boolean",
                        "title": "The private schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            False
                        ]
                    },
                    "owner": {
                        "$id": "#/items/anyOf/0/properties/owner",
                        "type": "object",
                        "title": "The owner schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [],
                        "required": [
                            "login",
                            "id",
                            "node_id",
                            "avatar_url",
                            "gravatar_id",
                            "url",
                            "html_url",
                            "followers_url",
                            "following_url",
                            "gists_url",
                            "starred_url",
                            "subscriptions_url",
                            "organizations_url",
                            "repos_url",
                            "events_url",
                            "received_events_url",
                            "type",
                            "site_admin"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "login": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/login",
                                "type": "string",
                                "title": "The login schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "apitestingco"
                                ]
                            },
                            "id": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/id",
                                "type": "integer",
                                "title": "The id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": 0,
                                "examples": [
                                    64370038
                                ]
                            },
                            "node_id": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/node_id",
                                "type": "string",
                                "title": "The node_id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "MDQ6VXNlcjY0MzcwMDM4"
                                ]
                            },
                            "avatar_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/avatar_url",
                                "type": "string",
                                "title": "The avatar_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://avatars3.githubusercontent.com/u/64370038?v=4"
                                ]
                            },
                            "gravatar_id": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/gravatar_id",
                                "type": "string",
                                "title": "The gravatar_id schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    ""
                                ]
                            },
                            "url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/url",
                                "type": "string",
                                "title": "The url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco"
                                ]
                            },
                            "html_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/html_url",
                                "type": "string",
                                "title": "The html_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://github.com/apitestingco"
                                ]
                            },
                            "followers_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/followers_url",
                                "type": "string",
                                "title": "The followers_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/followers"
                                ]
                            },
                            "following_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/following_url",
                                "type": "string",
                                "title": "The following_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/following{/other_user}"
                                ]
                            },
                            "gists_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/gists_url",
                                "type": "string",
                                "title": "The gists_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/gists{/gist_id}"
                                ]
                            },
                            "starred_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/starred_url",
                                "type": "string",
                                "title": "The starred_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/starred{/owner}{/repo}"
                                ]
                            },
                            "subscriptions_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/subscriptions_url",
                                "type": "string",
                                "title": "The subscriptions_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/subscriptions"
                                ]
                            },
                            "organizations_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/organizations_url",
                                "type": "string",
                                "title": "The organizations_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/orgs"
                                ]
                            },
                            "repos_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/repos_url",
                                "type": "string",
                                "title": "The repos_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/repos"
                                ]
                            },
                            "events_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/events_url",
                                "type": "string",
                                "title": "The events_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/events{/privacy}"
                                ]
                            },
                            "received_events_url": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/received_events_url",
                                "type": "string",
                                "title": "The received_events_url schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "https://api.github.com/users/apitestingco/received_events"
                                ]
                            },
                            "type": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/type",
                                "type": "string",
                                "title": "The type schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": "",
                                "examples": [
                                    "User"
                                ]
                            },
                            "site_admin": {
                                "$id": "#/items/anyOf/0/properties/owner/properties/site_admin",
                                "type": "boolean",
                                "title": "The site_admin schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": False,
                                "examples": [
                                    False
                                ]
                            }
                        }
                    },
                    "html_url": {
                        "$id": "#/items/anyOf/0/properties/html_url",
                        "type": "string",
                        "title": "The html_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://github.com/apitestingco/helloapi"
                        ]
                    },
                    "description": {
                        "$id": "#/items/anyOf/0/properties/description",
                        "type": "string",
                        "title": "The description schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "Hello API"
                        ]
                    },
                    "fork": {
                        "$id": "#/items/anyOf/0/properties/fork",
                        "type": "boolean",
                        "title": "The fork schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            False
                        ]
                    },
                    "url": {
                        "$id": "#/items/anyOf/0/properties/url",
                        "type": "string",
                        "title": "The url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi"
                        ]
                    },
                    "forks_url": {
                        "$id": "#/items/anyOf/0/properties/forks_url",
                        "type": "string",
                        "title": "The forks_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/forks"
                        ]
                    },
                    "keys_url": {
                        "$id": "#/items/anyOf/0/properties/keys_url",
                        "type": "string",
                        "title": "The keys_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/keys{/key_id}"
                        ]
                    },
                    "collaborators_url": {
                        "$id": "#/items/anyOf/0/properties/collaborators_url",
                        "type": "string",
                        "title": "The collaborators_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/collaborators{/collaborator}"
                        ]
                    },
                    "teams_url": {
                        "$id": "#/items/anyOf/0/properties/teams_url",
                        "type": "string",
                        "title": "The teams_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/teams"
                        ]
                    },
                    "hooks_url": {
                        "$id": "#/items/anyOf/0/properties/hooks_url",
                        "type": "string",
                        "title": "The hooks_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/hooks"
                        ]
                    },
                    "issue_events_url": {
                        "$id": "#/items/anyOf/0/properties/issue_events_url",
                        "type": "string",
                        "title": "The issue_events_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/issues/events{/number}"
                        ]
                    },
                    "events_url": {
                        "$id": "#/items/anyOf/0/properties/events_url",
                        "type": "string",
                        "title": "The events_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/events"
                        ]
                    },
                    "assignees_url": {
                        "$id": "#/items/anyOf/0/properties/assignees_url",
                        "type": "string",
                        "title": "The assignees_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/assignees{/user}"
                        ]
                    },
                    "branches_url": {
                        "$id": "#/items/anyOf/0/properties/branches_url",
                        "type": "string",
                        "title": "The branches_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/branches{/branch}"
                        ]
                    },
                    "tags_url": {
                        "$id": "#/items/anyOf/0/properties/tags_url",
                        "type": "string",
                        "title": "The tags_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/tags"
                        ]
                    },
                    "blobs_url": {
                        "$id": "#/items/anyOf/0/properties/blobs_url",
                        "type": "string",
                        "title": "The blobs_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/git/blobs{/sha}"
                        ]
                    },
                    "git_tags_url": {
                        "$id": "#/items/anyOf/0/properties/git_tags_url",
                        "type": "string",
                        "title": "The git_tags_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/git/tags{/sha}"
                        ]
                    },
                    "git_refs_url": {
                        "$id": "#/items/anyOf/0/properties/git_refs_url",
                        "type": "string",
                        "title": "The git_refs_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/git/refs{/sha}"
                        ]
                    },
                    "trees_url": {
                        "$id": "#/items/anyOf/0/properties/trees_url",
                        "type": "string",
                        "title": "The trees_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/git/trees{/sha}"
                        ]
                    },
                    "statuses_url": {
                        "$id": "#/items/anyOf/0/properties/statuses_url",
                        "type": "string",
                        "title": "The statuses_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/statuses/{sha}"
                        ]
                    },
                    "languages_url": {
                        "$id": "#/items/anyOf/0/properties/languages_url",
                        "type": "string",
                        "title": "The languages_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/languages"
                        ]
                    },
                    "stargazers_url": {
                        "$id": "#/items/anyOf/0/properties/stargazers_url",
                        "type": "string",
                        "title": "The stargazers_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/stargazers"
                        ]
                    },
                    "contributors_url": {
                        "$id": "#/items/anyOf/0/properties/contributors_url",
                        "type": "string",
                        "title": "The contributors_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/contributors"
                        ]
                    },
                    "subscribers_url": {
                        "$id": "#/items/anyOf/0/properties/subscribers_url",
                        "type": "string",
                        "title": "The subscribers_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/subscribers"
                        ]
                    },
                    "subscription_url": {
                        "$id": "#/items/anyOf/0/properties/subscription_url",
                        "type": "string",
                        "title": "The subscription_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/subscription"
                        ]
                    },
                    "commits_url": {
                        "$id": "#/items/anyOf/0/properties/commits_url",
                        "type": "string",
                        "title": "The commits_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/commits{/sha}"
                        ]
                    },
                    "git_commits_url": {
                        "$id": "#/items/anyOf/0/properties/git_commits_url",
                        "type": "string",
                        "title": "The git_commits_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/git/commits{/sha}"
                        ]
                    },
                    "comments_url": {
                        "$id": "#/items/anyOf/0/properties/comments_url",
                        "type": "string",
                        "title": "The comments_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/comments{/number}"
                        ]
                    },
                    "issue_comment_url": {
                        "$id": "#/items/anyOf/0/properties/issue_comment_url",
                        "type": "string",
                        "title": "The issue_comment_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/issues/comments{/number}"
                        ]
                    },
                    "contents_url": {
                        "$id": "#/items/anyOf/0/properties/contents_url",
                        "type": "string",
                        "title": "The contents_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/contents/{+path}"
                        ]
                    },
                    "compare_url": {
                        "$id": "#/items/anyOf/0/properties/compare_url",
                        "type": "string",
                        "title": "The compare_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/compare/{base}...{head}"
                        ]
                    },
                    "merges_url": {
                        "$id": "#/items/anyOf/0/properties/merges_url",
                        "type": "string",
                        "title": "The merges_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/merges"
                        ]
                    },
                    "archive_url": {
                        "$id": "#/items/anyOf/0/properties/archive_url",
                        "type": "string",
                        "title": "The archive_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/{archive_format}{/ref}"
                        ]
                    },
                    "downloads_url": {
                        "$id": "#/items/anyOf/0/properties/downloads_url",
                        "type": "string",
                        "title": "The downloads_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/downloads"
                        ]
                    },
                    "issues_url": {
                        "$id": "#/items/anyOf/0/properties/issues_url",
                        "type": "string",
                        "title": "The issues_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/issues{/number}"
                        ]
                    },
                    "pulls_url": {
                        "$id": "#/items/anyOf/0/properties/pulls_url",
                        "type": "string",
                        "title": "The pulls_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/pulls{/number}"
                        ]
                    },
                    "milestones_url": {
                        "$id": "#/items/anyOf/0/properties/milestones_url",
                        "type": "string",
                        "title": "The milestones_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/milestones{/number}"
                        ]
                    },
                    "notifications_url": {
                        "$id": "#/items/anyOf/0/properties/notifications_url",
                        "type": "string",
                        "title": "The notifications_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/notifications{?since,all,participating}"
                        ]
                    },
                    "labels_url": {
                        "$id": "#/items/anyOf/0/properties/labels_url",
                        "type": "string",
                        "title": "The labels_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/labels{/name}"
                        ]
                    },
                    "releases_url": {
                        "$id": "#/items/anyOf/0/properties/releases_url",
                        "type": "string",
                        "title": "The releases_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/releases{/id}"
                        ]
                    },
                    "deployments_url": {
                        "$id": "#/items/anyOf/0/properties/deployments_url",
                        "type": "string",
                        "title": "The deployments_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://api.github.com/repos/apitestingco/helloapi/deployments"
                        ]
                    },
                    "created_at": {
                        "$id": "#/items/anyOf/0/properties/created_at",
                        "type": "string",
                        "title": "The created_at schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "2020-04-26T16:15:12Z"
                        ]
                    },
                    "updated_at": {
                        "$id": "#/items/anyOf/0/properties/updated_at",
                        "type": "string",
                        "title": "The updated_at schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "2020-04-26T16:15:16Z"
                        ]
                    },
                    "pushed_at": {
                        "$id": "#/items/anyOf/0/properties/pushed_at",
                        "type": "string",
                        "title": "The pushed_at schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "2020-04-26T16:15:14Z"
                        ]
                    },
                    "git_url": {
                        "$id": "#/items/anyOf/0/properties/git_url",
                        "type": "string",
                        "title": "The git_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "git://github.com/apitestingco/helloapi.git"
                        ]
                    },
                    "ssh_url": {
                        "$id": "#/items/anyOf/0/properties/ssh_url",
                        "type": "string",
                        "title": "The ssh_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "git@github.com:apitestingco/helloapi.git"
                        ]
                    },
                    "clone_url": {
                        "$id": "#/items/anyOf/0/properties/clone_url",
                        "type": "string",
                        "title": "The clone_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://github.com/apitestingco/helloapi.git"
                        ]
                    },
                    "svn_url": {
                        "$id": "#/items/anyOf/0/properties/svn_url",
                        "type": "string",
                        "title": "The svn_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "https://github.com/apitestingco/helloapi"
                        ]
                    },
                    "size": {
                        "$id": "#/items/anyOf/0/properties/size",
                        "type": "integer",
                        "title": "The size schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "stargazers_count": {
                        "$id": "#/items/anyOf/0/properties/stargazers_count",
                        "type": "integer",
                        "title": "The stargazers_count schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "watchers_count": {
                        "$id": "#/items/anyOf/0/properties/watchers_count",
                        "type": "integer",
                        "title": "The watchers_count schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "has_issues": {
                        "$id": "#/items/anyOf/0/properties/has_issues",
                        "type": "boolean",
                        "title": "The has_issues schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            True
                        ]
                    },
                    "has_projects": {
                        "$id": "#/items/anyOf/0/properties/has_projects",
                        "type": "boolean",
                        "title": "The has_projects schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            True
                        ]
                    },
                    "has_downloads": {
                        "$id": "#/items/anyOf/0/properties/has_downloads",
                        "type": "boolean",
                        "title": "The has_downloads schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            True
                        ]
                    },
                    "has_wiki": {
                        "$id": "#/items/anyOf/0/properties/has_wiki",
                        "type": "boolean",
                        "title": "The has_wiki schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            True
                        ]
                    },
                    "has_pages": {
                        "$id": "#/items/anyOf/0/properties/has_pages",
                        "type": "boolean",
                        "title": "The has_pages schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            False
                        ]
                    },
                    "forks_count": {
                        "$id": "#/items/anyOf/0/properties/forks_count",
                        "type": "integer",
                        "title": "The forks_count schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "mirror_url": {
                        "$id": "#/items/anyOf/0/properties/mirror_url",
                        "type": "null",
                        "title": "The mirror_url schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": None,
                        "examples": [
                            None
                        ]
                    },
                    "archived": {
                        "$id": "#/items/anyOf/0/properties/archived",
                        "type": "boolean",
                        "title": "The archived schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            False
                        ]
                    },
                    "disabled": {
                        "$id": "#/items/anyOf/0/properties/disabled",
                        "type": "boolean",
                        "title": "The disabled schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": False,
                        "examples": [
                            False
                        ]
                    },
                    "open_issues_count": {
                        "$id": "#/items/anyOf/0/properties/open_issues_count",
                        "type": "integer",
                        "title": "The open_issues_count schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "license": {
                        "$id": "#/items/anyOf/0/properties/license",
                        "type": "null",
                        "title": "The license schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": None,
                        "examples": [
                            None
                        ]
                    },
                    "forks": {
                        "$id": "#/items/anyOf/0/properties/forks",
                        "type": "integer",
                        "title": "The forks schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "open_issues": {
                        "$id": "#/items/anyOf/0/properties/open_issues",
                        "type": "integer",
                        "title": "The open_issues schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "watchers": {
                        "$id": "#/items/anyOf/0/properties/watchers",
                        "type": "integer",
                        "title": "The watchers schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": 0,
                        "examples": [
                            0
                        ]
                    },
                    "default_branch": {
                        "$id": "#/items/anyOf/0/properties/default_branch",
                        "type": "string",
                        "title": "The default_branch schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": "",
                        "examples": [
                            "master"
                        ]
                    },
                    "permissions": {
                        "$id": "#/items/anyOf/0/properties/permissions",
                        "type": "object",
                        "title": "The permissions schema",
                        "description": "An explanation about the purpose of this instance.",
                        "default": {},
                        "examples": [
                            {
                                "admin": True,
                                "push": True,
                                "pull": True
                            }
                        ],
                        "required": [
                            "admin",
                            "push",
                            "pull"
                        ],
                        "additionalProperties": True,
                        "properties": {
                            "admin": {
                                "$id": "#/items/anyOf/0/properties/permissions/properties/admin",
                                "type": "boolean",
                                "title": "The admin schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": False,
                                "examples": [
                                    True
                                ]
                            },
                            "push": {
                                "$id": "#/items/anyOf/0/properties/permissions/properties/push",
                                "type": "boolean",
                                "title": "The push schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": False,
                                "examples": [
                                    True
                                ]
                            },
                            "pull": {
                                "$id": "#/items/anyOf/0/properties/permissions/properties/pull",
                                "type": "boolean",
                                "title": "The pull schema",
                                "description": "An explanation about the purpose of this instance.",
                                "default": False,
                                "examples": [
                                    True
                                ]
                            }
                        }
                    }
                }
            }
        ],
        "$id": "#/items"
    }
}
