# Manage policies in ACS with Ansible

## Challenge

We want to manage ACS policies in a GitOps fashion with two major goals:

1.  All policies are stored in git and version controlled.
2.  Policies can be created using the ACS Central GUI.

## Solution

This project implements an Ansible-based solution that will

1.  Pull desired configuration from a git repo.
2.  Pull the current configuration from ACS.
3.  Change current policies to the desired state.
4.  Create a new branch in the git repo with any changes that were made.

This meets our goals as any new policies created in the UI are reflected in the new branch which can, then, be merged into `main` via a pull request.

## Prep

Create a new git repo and initialize it with a README.md.  Create a Personal Access Token (PAT) that can read from & write to the repo.

Create an ACS API token.  The ACS API token can either have the Admin role or, if you prefer, a custom role with read/write permission to the /policies API endpoint.  More info can be found [here](https://docs.openshift.com/acs/3.67/cli/getting-started-cli.html#cli-authentication_cli-getting-started).

Install Ansible Galaxy requirements with `ansible-galaxy install -r requirements.yml`.

## Ansible

Create your Ansible Vault with those variables:

```yaml
vaulted_acs_host: <your-acs-host>
vaulted_acs_token: <your-acs-API-token>
vaulted_git_user: <git user with read/write access>
vaulted_git_pat: <git PAT>
vaulted_git_url: <http URL to the git repo>
```

Run the `initial.yml` playbook to create the desired policy collection

```bash
ansible-playbook --ask-vault-pass initial.yml
```

When needed, execute the `update.yml` playbook to compare actual policies to desired, ensure that desired policies are applied, and create a new branch with any changes.

```bash
ansible-playbook --ask-vault-pass update.yml
```

If desired, this could be triggered by ACS audit log entries for policy changes and/or by git webhooks on updates to the `main` branch.

