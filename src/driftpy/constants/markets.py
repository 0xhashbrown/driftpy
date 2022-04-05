from dataclasses import dataclass


@dataclass
class Market:
    symbol: str
    base_asset_symbol: str
    market_index: int
    devnet_pyth_oracle: str
    mainnet_pyth_oracle: str


MARKETS: list[Market] = [
    Market(
        symbol="SOL-PERP",
        base_asset_symbol="SOL",
        market_index=0,
        devnet_pyth_oracle="J83w4HKfqxwcq3BEMMkPFSppX3gqekLyLJBexebFVkix",
        mainnet_pyth_oracle="H6ARHf6YXhGYeQfUzQNGk6rDNnLBQKrenN712K4AQJEG",
    ),
    Market(
        symbol="BTC-PERP",
        base_asset_symbol="BTC",
        market_index=1,
        devnet_pyth_oracle="HovQMDrbAgAYPCmHVSrezcSmkMtXSSUsLDFANExrZh2J",
        mainnet_pyth_oracle="GVXRSBjFk6e6J3NbVPXohDJetcTjaeeuykUpbQF8UoMU",
    ),
    Market(
        symbol="ETH-PERP",
        base_asset_symbol="ETH",
        market_index=2,
        devnet_pyth_oracle="EdVCmQ9FSPcVe5YySXDPCRmc8aDQLKJ9xvYBMZPie1Vw",
        mainnet_pyth_oracle="JBu1AL4obBcCMqKBBxhpWCNUt136ijcuMZLFvTP7iWdB",
    ),
    Market(
        symbol="LUNA-PERP",
        base_asset_symbol="LUNA",
        market_index=3,
        devnet_pyth_oracle="8PugCXTAHLM9kfLSQWe2njE5pzAgUdpPk3Nx5zSm7BD3",
        mainnet_pyth_oracle="5bmWuR1dgP4avtGYMNKLuxumZTVKGgoN2BCMXWDNL9nY",
    ),
    Market(
        symbol="AVAX-PERP",
        base_asset_symbol="AVAX",
        market_index=4,
        devnet_pyth_oracle="FVb5h1VmHPfVb1RfqZckchq18GxRv4iKt8T4eVTQAqdz",
        mainnet_pyth_oracle="Ax9ujW5B9oqcv59N8m6f1BpTBq2rGeGaBcpKjC5UYsXU",
    ),
    Market(
        symbol="BNB-PERP",
        base_asset_symbol="BNB",
        market_index=5,
        devnet_pyth_oracle="GwzBgrXb4PG59zjce24SF2b9JXbLEjJJTBkmytuEZj1b",
        mainnet_pyth_oracle="4CkQJBxhU8EZ2UjhigbtdaPbpTe6mqf811fipYBFbSYN",
    ),
    Market(
        symbol="MATIC-PERP",
        base_asset_symbol="MATIC",
        market_index=6,
        devnet_pyth_oracle="FBirwuDFuRAu4iSGc7RGxN5koHB7EJM1wbCmyPuQoGur",
        mainnet_pyth_oracle="7KVswB9vkCgeM3SHP7aGDijvdRAHK8P5wi9JXViCrtYh",
    ),
    Market(
        symbol="ATOM-PERP",
        base_asset_symbol="ATOM",
        market_index=7,
        devnet_pyth_oracle="7YAze8qFUMkBnyLVdKT4TFUUFui99EwS5gfRArMcrvFk",
        mainnet_pyth_oracle="CrCpTerNqtZvqLcKqz1k13oVeXV9WkMD2zA9hBKXrsbN",
    ),
    Market(
        symbol="DOT-PERP",
        base_asset_symbol="DOT",
        market_index=8,
        devnet_pyth_oracle="4dqq5VBpN4EwYb7wyywjjfknvMKu7m78j9mKZRXTj462",
        mainnet_pyth_oracle="EcV1X1gY2yb4KXxjVQtTHTbioum2gvmPnFk4zYAt7zne",
    ),
    Market(
        symbol="ADA-PERP",
        base_asset_symbol="ADA",
        market_index=9,
        devnet_pyth_oracle="8oGTURNmSQkrBS1AQ5NjB2p8qY34UVmMA9ojrw8vnHus",
        mainnet_pyth_oracle="3pyn4svBbxJ9Wnn3RVeafyLWfzie6yC5eTig2S62v9SC",
        # launch_ts=1643084413000,
    ),
    Market(
        symbol="ALGO-PERP",
        base_asset_symbol="ALGO",
        market_index=10,
        devnet_pyth_oracle="c1A946dY5NHuVda77C8XXtXytyR3wK1SCP3eA9VRfC3",
        mainnet_pyth_oracle="HqFyq1wh1xKvL7KDqqT7NJeSPdAqsDqnmBisUC2XdXAX",
        # launch_ts: 1643686767000,
    ),
    Market(
        symbol="FTT-PERP",
        base_asset_symbol="FTT",
        market_index=11,
        devnet_pyth_oracle="6vivTRs5ZPeeXbjo7dfburfaYDWoXjBtdtuYgQRuGfu",
        mainnet_pyth_oracle="8JPJJkmDScpcNmBRKGZuPuG2GYAveQgP3t5gFuMymwvF",
        # launch_ts: 1643686767000,
    ),
    Market(
        symbol="LTC-PERP",
        base_asset_symbol="LTC",
        market_index=12,
        devnet_pyth_oracle="BLArYBCUYhdWiY8PCUTpvFE21iaJq85dvxLk9bYMobcU",
        mainnet_pyth_oracle="8RMnV1eD55iqUFJLMguPkYBkq8DCtx81XcmAja93LvRR",
        # launch_ts: 1643686767000,
    ),
    Market(
        symbol="XRP-PERP",
        base_asset_symbol="XRP",
        market_index=13,
        devnet_pyth_oracle="WMW5xc3HypXwTnPesyUT49uLsyHwNURsWAEk39onKuk",
        mainnet_pyth_oracle="WMW5xc3HypXwTnPesyUT49uLsyHwNURsWAEk39onKuk",
        # launchTs: 1647543166000,
		# oracleSource: OracleSource.SWITCHBOARD,    
    ),
    Market(
        symbol="APE-PERP",
        base_asset_symbol="APE",
        market_index=14,
        devnet_pyth_oracle="AwH6kBrJbkL9JTeqRd7Q59EdWh6UjPtoqoA5M4x4K2fA",
        mainnet_pyth_oracle="74zeQpprjNtEghGiC3VEPsR9y4kR2GTd4Rq9YVk9tnjz",
        # launchTs: 1648475932000,
		# oracleSource: OracleSource.SWITCHBOARD,    
    ),
    Market(
        symbol="DOGE-PERP",
        base_asset_symbol="DOGE",
        market_index=15,
        devnet_pyth_oracle="4L6YhY8VvUgmqG5MvJkUJATtzB2rFqdrJwQCmFLv4Jzy",
        mainnet_pyth_oracle="FsSM3s38PX9K7Dn6eGzuE29S2Dsk1Sss1baytTQdCaQj",
        # launchTs: 1648607439000,
		# oracleSource: OracleSource.PYTH,    
    ),
    Market(
        symbol="NEAR-PERP",
        base_asset_symbol="NEAR",
        market_index=16,
        devnet_pyth_oracle="3gnSbT7bhoTdGkFVZc1dW1PvjreWzpUNUD5ppXwv1N59",
        mainnet_pyth_oracle="ECSFWQ1bnnpqPVvoy9237t2wddZAaHisW88mYxuEHKWf",
        # launchTs: 1649105516000,
		# oracleSource: OracleSource.PYTH,    
    ),
]
