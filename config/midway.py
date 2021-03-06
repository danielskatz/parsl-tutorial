from parsl.config import Config

from parsl.providers import SlurmProvider
from parsl.channels import LocalChannel
from parsl.executors import HighThroughputExecutor
from parsl.launchers import SingleNodeLauncher
from parsl.addresses import address_by_hostname

from parsl.data_provider.scheme import GlobusScheme

config = Config(
    executors=[
        HighThroughputExecutor(
            label="midway_htex",
            worker_debug=True,
            address=address_by_hostname(),
            provider=SlurmProvider(
                'broadwl',
                launcher=SingleNodeLauncher(),
                worker_init='source activate parsl_dev',
                init_blocks=1,
                max_blocks=1,
                min_blocks=1,
                nodes_per_block=1,
                walltime='0:30:00'
            ),
            storage_access=[GlobusScheme(
                endpoint_uuid="af7bda53-6d04-11e5-ba46-22000b92c6ec",
                endpoint_path="/",
                local_path="/"
            )]
        )
    ],
)