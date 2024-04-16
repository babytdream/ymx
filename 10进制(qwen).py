history = [(
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "2015-10-14 07:22:38", "from": "0x2a65aca4d5fc5b5c859090a6c34d164135398226(DwarfPol)", "to": "0x555be1ef013616269aabab18335c2ec40702b5ed",  "value": "4791110000000000000 ", "gasUsed": 21000, "gasPrice": 50000000000}""",
               """DwarfPool sent 4.79 Ether to 0x555be1...0702b5Ed with a transaction fee of 0.001 Ether at Oct-14-2015 07:22:38 AM +UTC."""),
           (
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "2015-08-14 22:04:59", "from": "0x7871c9936a21b89507b5b65c7b13d8216d832d76", "to": "0x108fedb097c1dcfed441480170144d8e19bb217f(Poloniex_Deposit_0x108f)", "value": "100000000000000000 ", "gasUsed": 21000, "gasPrice": 54702850138}""",
               """0x7871C9...6D832D76 sent 0.1 Ether to Poloniex_Deposit_0x108f with a transaction fee of 0.0011 Ether at Aug-14-2015 10:04:59 PM +UTC."}"""),
           (
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "2015-08-28 16:59:27", "from": "0x007f7f58d3eb5b7510a301ecc749fc1fcddbe14d", "to": "0xb1abce2918e21ddb93aa452731a12672a3d9f75a", "value": "5000000000000000000 ", "gasUsed": 21000, "gasPrice": 50000000000}""",
               """0x007f7f...CDDBE14D sent 5 Ether to 0xb1abce...A3d9F75a with a transaction fee of 0.001 Ether at Aug-28-2015 04:59:27 PM +UTC."""),
           (
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "2015-11-13 09:15:08", "from": "0x54cec426307c1acaa63b25aa48fade5df9e5d418", "to": "0xc47aaa860008be6f65b58c6c6e02a84e666efe31", "value": "21965300000000000 ", "gasUsed": 21000, "gasPrice": 50000000000}""",
               """0x54ceC4...f9e5D418 sent 0.022 Ether to 0xC47Aaa...666EfE31 with a transaction fee of 0.001 Ether at Nov-13-2015 09:15:08 AM +UTC."""),
           (
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "2015-09-17 12:43:10", "from": "0x1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe(Suprnova)", "to": "0x77e41b4125b7c14757e0f07fe36b2e95db757a10(Kraken_Deposit_0x77e4)", "value": "6006980000000000000 ", "gasUsed": 21000, "gasPrice": 50000000000}""",
               """Suprnova sent 6.01 Ether to Kraken_Deposit_0x77e4 with a transaction fee of 0.001 Ether at Sep-17-2015 12:43:10 PM +UTC."""), ]
query = [
            """{"timestamp": "2015-09-03 07:09:40", "from": "0xe6a7a1d47ff21b6321162aea7c6cb457d5476bca(Ethpool)", "to": "0x0d3111e6cfa28bc8745057bd71e0d10feb4c7ae7", "value": "2788520000000000000 ", "gasUsed": 21000, "gasPrice": 40000000000}""",

            """{"timestamp": "2015-10-04 21:05:07", "from": "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5(Nanopool)", "to": "0x378fcaef49580b550cb7164f14811a5e613bd683(Poloniex_Deposit_0x378f)", "value": "3381420000000000000 ", "gasUsed": 21000, "gasPrice": 30000000000}""",

            """{"timestamp": "2015-12-13 12:25:30", "from": "0xe996d36db289ef8d9f0a9f9a903cc42fea50cd4e", "to": "0xc47aaa860008be6f65b58c6c6e02a84e666efe31", "value": "516310000000000000 ", "gasUsed": 21000, "gasPrice": 20000000000}""",

            """{"timestamp": "2015-10-09 08:59:58", "from": "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5(Nanopool)", "to": "0x33e1a1ae6d566e20dc21f247126981d001b659ce(Bittrex_Deposit_0x33e1)", "value": "800993000000000000 ", "gasUsed": 21000, "gasPrice": 10000000000}""",

            """{ "timestamp":"2015-12-09 09:25:41", "from": "0x5cfea98867469500b90f0aa18402b95531869662", "to": "0x32be343b94f860124dc4fee278fdcbd38c102d88(Poloniex)", "value": "4962050000000000000 ", "gasUsed": 21000, "gasPrice": 60000000000}""",
        ]
result = [
              """GPT:Ethpool sent 2.79 Ether to 0x0D3111...EB4C7AE7 with a transaction fee of 0.00084 Ether at Sep-03-2015 07:09:40 AM +UTC.""",
              """GPT:Nanopool sent 3.38 Ether to Poloniex_Deposit_0x378f with a transaction fee of 0.00063 Ether at Oct-04-2015 09:05:07 PM +UTC.""",
              """GPT:0xE996d3...EA50CD4E sent 0.52 Ether to 0xC47Aaa...666EfE31 with a transaction fee of 0.00042 Ether at Dec-13-2015 12:25:30 PM +UTC.""",
              """GPT:Nanopool sent 0.8 Ether to Bittrex_Deposit_0x33e1 with a transaction fee of 0.00021 Ether at Oct-09-2015 08:59:58 AM +UTC.""",
              """GPT:0x5cFEa9...31869662 sent 4.96 Ether to Poloniex with a transaction fee of 0.0013 Ether at Dec-09-2015 09:25:41 AM +UTC.""",]
for i,j in zip(query,result):
    response, history = model.chat(tokenizer, i,history=history)
    print(response,'\n',j)