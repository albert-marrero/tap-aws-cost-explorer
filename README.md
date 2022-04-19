# tap-aws-cost-explorer

`tap-aws-cost-explorer` is a Singer tap for AWSCostExplorer.

Built with the [Meltano Tap SDK](https://sdk.meltano.com) for Singer Taps.

## Installation

```bash
pipx install git+https://github.com/albert-marrero/tap-aws-cost-explorer
```

## Configuration
A full list of supported settings and capabilities for this
tap is available by running:

```bash
tap-aws-cost-explorer --about
```

### Capabilities

* `sync`
* `catalog`
* `state`
* `discover`

### Source Authentication and Authorization

You will need to [create an IAM user account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) in Your AWS Account with [access to Cost Explorer.](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/ce-access.html#ce-iam-users)

After you created the desired IAM user account, you need [access keys](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys) to make programmatic calls to AWS.

### Configuration
```json
{
    "access_key": "ACCESS_KEY",
    "secret_key": "SECRET_ACCESS_KEY",
    "session_token": "SESSION_TOKEN",
    "start_date": "2020-10-01",
    "end_date": "2021-09-01",
    "granularity": "DAILY",
    "metrics": ["AmortizedCost", "BlendedCost", "NetAmortizedCost", "NetUnblendedCost", "NormalizedUsageAmount", "UnblendedCost", "UsageQuantity"]
}
```
A bit of a run down on each of the properties:
- **access_key**: Your AWS Account Access Key.
- **secret_key**: Your AWS Account Secret Key.
- **session_token** (Optional): Your AWS Account Secret Key.
- **start_date**: The start date for retrieving Amazon Web Services cost. Can only be a maximum of 12 months previously.
- **end_date** (Optional): The end date for retrieving Amazon Web Services cost, defaults to yesterday.
- **granularity**: Sets the Amazon Web Services cost granularity to MONTHLY or DAILY , or HOURLY.
- **metrics**: Which metrics are returned in the query. Valid values are AmortizedCost, BlendedCost, NetAmortizedCost, NetUnblendedCost, NormalizedUsageAmount, UnblendedCost, and UsageQuantity."

## Usage

You can easily run `tap-aws-cost-explorer` by itself or in a pipeline using [Meltano](https://meltano.com/).

### Executing the Tap Directly

```bash
tap-aws-cost-explorer --version
tap-aws-cost-explorer --help
tap-aws-cost-explorer --config CONFIG --discover > ./catalog.json
```

## Developer Resources

### Initialize your Development Environment

```bash
pipx install poetry
poetry install
```

### Create and Run Tests

Create tests within the `tap_aws_cost_explorer/tests` subfolder and
  then run:

```bash
poetry run pytest
```

You can also test the `tap-aws-cost-explorer` CLI interface directly using `poetry run`:

```bash
poetry run tap-aws-cost-explorer --help
```

### Testing with [Meltano](https://www.meltano.com)

_**Note:** This tap will work in any Singer environment and does not require Meltano.
Examples here are for convenience and to streamline end-to-end orchestration scenarios._

Your project comes with a custom `meltano.yml` project file already created. Open the `meltano.yml` and follow any _"TODO"_ items listed in
the file.

Next, install Meltano (if you haven't already) and any needed plugins:

```bash
# Install meltano
pipx install meltano
# Initialize meltano within this directory
cd tap-aws-cost-explorer
meltano install
```

Now you can test and orchestrate using Meltano:

```bash
# Test invocation:
meltano invoke tap-aws-cost-explorer --version
# OR run a test `elt` pipeline:
meltano elt tap-aws-cost-explorer target-jsonl
```

### SDK Dev Guide

See the [dev guide](https://sdk.meltano.com/en/latest/dev_guide.html) for more instructions on how to use the SDK to 
develop your own taps and targets.

## Contributing
For major changes, please open an issue first to discuss what you would like to change.

## Support
If you enjoy this repository, please [star](https://docs.github.com/en/get-started/exploring-projects-on-github/saving-repositories-with-stars) this repository. By starring a repository, it shows appreciation to the repository maintainer for their work. Many of GitHub's repository rankings depend on the number of stars a repository has.

## License
[MIT](LICENSE)