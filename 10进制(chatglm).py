history = [[
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "1444807358", "from": "0x2a65aca4d5fc5b5c859090a6c34d164135398226(DwarfPol)", "to": "0x555be1ef013616269aabab18335c2ec40702b5ed", "value": "0x427d71291dd26000", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}""",
               """DwarfPool sent 4.79 Ether to 0x555be1...0702b5Ed with a transaction fee of 0.001 Ether at Oct-14-2015 07:22:38 AM +UTC."""],
           [
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "1439589899", "from": "0x7871c9936a21b89507b5b65c7b13d8216d832d76", "to": "0x108fedb097c1dcfed441480170144d8e19bb217f(Poloniex_Deposit_0x108f)", "value": "0x16345785d8a0000", "gasUsed": "0x5208", "gasPrice": "0xcbc8b405a"}""",
               """0x7871C9...6D832D76 sent 0.1 Ether to Poloniex_Deposit_0x108f with a transaction fee of 0.0011 Ether at Aug-14-2015 10:04:59 PM +UTC."}"""],
           [
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "1440781167", "from": "0x007f7f58d3eb5b7510a301ecc749fc1fcddbe14d", "to": "0xb1abce2918e21ddb93aa452731a12672a3d9f75a", "value": "0x4563918244f40000", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}""",
               """0x007f7f...CDDBE14D sent 5 Ether to 0xb1abce...A3d9F75a with a transaction fee of 0.001 Ether at Aug-28-2015 04:59:27 PM +UTC."""],
           [
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "1447406108", "from": "0x54cec426307c1acaa63b25aa48fade5df9e5d418", "to": "0xc47aaa860008be6f65b58c6c6e02a84e666efe31", "value": "0x4e0952efe28800", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}""",
               """0x54ceC4...f9e5D418 sent 0.022 Ether to 0xC47Aaa...666EfE31 with a transaction fee of 0.001 Ether at Nov-13-2015 09:15:08 AM +UTC."""],
           [
               """Summarize this Ethereum transaction in one sentence:{"timestamp": "1442493790", "from": "0x1dcb8d1f0fcc8cbc8c2d76528e877f915e299fbe(Suprnova)", "to": "0x77e41b4125b7c14757e0f07fe36b2e95db757a10(Kraken_Deposit_0x77e4)", "value": "0x535d147bd0e04000", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}""",
               """Suprnova sent 6.01 Ether to Kraken_Deposit_0x77e4 with a transaction fee of 0.001 Ether at Sep-17-2015 12:43:10 PM +UTC."""], ]
text = [[
            """{"timestamp": "1441264180", "from": "0xe6a7a1d47ff21b6321162aea7c6cb457d5476bca(Ethpool)", "to": "0x0d3111e6cfa28bc8745057bd71e0d10feb4c7ae7", "value": "0x26b2d02a71128000", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}"""],
        [
            """{"timestamp": "1443992707", "from": "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5(Nanopool)", "to": "0x378fcaef49580b550cb7164f14811a5e613bd683(Poloniex_Deposit_0x378f)", "value": "0x2eed37931066c000", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}"""],
        [
            """{"timestamp": "1450009530", "from": "0xe996d36db289ef8d9f0a9f9a903cc42fea50cd4e", "to": "0xc47aaa860008be6f65b58c6c6e02a84e666efe31", "value": "0x72a4d359ffb6000", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}"""],
        [
            """{"timestamp": "1444381198", "from": "0x52bc44d5378309ee2abf1539bf71de1b7d7be3b5(Nanopool)", "to": "0x33e1a1ae6d566e20dc21f247126981d001b659ce(Bittrex_Deposit_0x33e1)", "value": "0xb1db2e3c0931000", "gasUsed": "0x5208", "gasPrice": "0xba43b7400"}"""],
        [
            """{ "timestamp":"1449653141", "from": "0x5cfea98867469500b90f0aa18402b95531869662", "to": "0x32be343b94f860124dc4fee278fdcbd38c102d88(Poloniex)", "value": "0x44dcbe2f57ba2000", "gasUsed": "0x5208", "gasPrice": "0xdf8475800"}"""],
        ]
result = [[
              """GPT:Ethpool sent 2.79 Ether to 0x0D3111...EB4C7AE7 with a transaction fee of 0.001 Ether at Sep-03-2015 07:09:40 AM +UTC."""],
          [
              """GPT:Nanopool sent 3.38 Ether to Poloniex_Deposit_0x378f with a transaction fee of 0.001 Ether at Oct-04-2015 09:05:07 PM +UTC."""],
          [
              """GPT:0xE996d3...EA50CD4E sent 0.52 Ether to 0xC47Aaa...666EfE31 with a transaction fee of 0.001 Ether at Dec-13-2015 12:25:30 PM +UTC."""],
          [
              """GPT:Nanopool sent 0.8 Ether to Bittrex_Deposit_0x33e1 with a transaction fee of 0.001 Ether at Oct-09-2015 08:59:58 AM +UTC."""],
          [
              """GPT:0x5cFEa9...31869662 sent 4.96 Ether to Poloniex with a transaction fee of 0.0013 Ether at Dec-09-2015 09:25:41 AM +UTC."""],
          ]
for i,j in zip(text,result):
    response, history = model.chat(tokenizer, i,history=history)
    print(response,'\n',j)