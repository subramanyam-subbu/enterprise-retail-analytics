from python.generators.campaign_generator import generate_campaign
from python.loaders.campaign_loader import load_campaign

TOTAL_CAMPAIGNS = 10


def run_pipeline():
    """
    Generate and load campaign data.
    """

    print("=" * 60)
    print("Campaign Pipeline Started")
    print("=" * 60)

    loaded = 0

    for index in range(TOTAL_CAMPAIGNS):

        campaign = generate_campaign(index)

        load_campaign(campaign)

        loaded += 1

        print(f"Campaign {loaded} loaded.")

    print("=" * 60)
    print("Pipeline Completed Successfully")
    print(f"Total Campaigns Loaded : {loaded}")
    print("=" * 60)


if __name__ == "__main__":
    run_pipeline()