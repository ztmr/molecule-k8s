# molecule-k8s

Allow Ansible Molecule scenarios to be executed in the Kubernetes cluster.

## Installing

```console
$ pip install molecule-k8s
```

## Usage

```console
$ molecule init scenario -d k8s
$ molecule test
```

## Testing

To execute unit tests.

```console
$ make dep
$ make test
```

