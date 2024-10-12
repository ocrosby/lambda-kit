# Semantic Release

The GitHub authentication configuration is required and can be set via environment variables.

Follow the Creating a personal access token for the command line documentation to obtain an authentication token. The token has to be made available in your CI environment via the GH_TOKEN environment variable. The user associated with the token must have push permission to the repository.

When creating the token, the **minimum required scopes** are:

* repo for a private repository
* public_repo for a public repository

Note on GitHub Actions: You can use the default token which is provided in the 
secret GITHUB_TOKEN. However releases done with this token will NOT trigger release 
events to start other workflows. If you have actions that trigger on newly created 
releases, please use a generated token for that and store it in your repository's 
secrets (any other name than GITHUB_TOKEN is fine).

When using the GITHUB_TOKEN, the **minimum required permissions** are:

* contents: write to be able to publish a GitHub release
* issues: write to be able to comment on released issues
* pull-requests: write to be able to comment on released pull requests

The scopes I set for my PAT are:

* repo
* repo:status
* repo_deployment
* public_repo
* repo:invite
* security_events
* workflow
* write:packages
* read:packages
* admin:repo_hook
* write:repo_hook
* read:repo_hook


## Environment variables

GITHUB_TOKEN or GH_TOKEN are required to authenticate with GitHub. The token must have push access to the repository.


## References

- [GitHub Authentication](https://github.com/semantic-release/github/blob/master/README.md#github-authentication)