"""K8s Driver Module."""

from __future__ import absolute_import

import subprocess
from typing import Dict

from molecule import logger
from molecule.api import Driver

log = logger.get_logger(__name__)


class K8s(Driver):
    """
    K8s Driver Class.

    The class responsible for managing `k8s`_.

    Molecule leverages Ansible's `command`_ module, by mapping
    variables from ``molecule.yml`` into ``create.yml`` and ``destroy.yml``.

    .. code-block:: yaml

        driver:
          name: k8s
        platforms:
          - name: default-centos7-${CI_JOB_ID}
            namespace: default
            image: centos:7
            privileged: true
            command: /sbin/init
    """  # noqa

    def __init__(self, config=None):
        """Construct k8s."""
        super(K8s, self).__init__(config)
        self._name = "k8s"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def login_cmd_template(self):
        return (
            "kubectl exec -ti -n {namespace} {instance} -- sh -c 'exec $SHELL'"
        )

    @property
    def default_safe_files(self):
        return []

    @property
    def default_ssh_connection_options(self):
        return []

    def login_options(self, instance_name):
        d = {"instance": instance_name}
        return util.merge_dicts(d, self._get_instance_config(instance_name))

    def ansible_connection_options(self, instance_name):
        return {"ansible_connection": "kubectl"}

    def sanity_checks(self):
        subprocess.run(
            "kubectl version",
            shell=True,
            check=True,
            stderr=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
        )
        pass

    def reset(self):
        pass

    @property
    def required_collections(self) -> Dict[str, str]:
        """Return collections dict containing names and versions required."""
        return {"community.kubernetes": "1.2.1"}
