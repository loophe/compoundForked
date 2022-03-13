
## Instuctions

The main point of this project is cTokenMinePool.sol and MonkeyContract.sol in ./contract. cTokenMinePool actually the operator contract of cToken from Compound protocol and NFT contract of MonkeyContract. 

I strongly recommend you setup brownie v1.17.2 and remix v0.22.0-dev first 

Before cTokenMinePool and MonkeyContract, you should deploy [forked compound protocol](https://github.com/loophe/cTokenMinePool/tree/master/contracts/compoundForked) on mainnet fork mode by above two or more. The tutoral is [here](https://github.com/Dapp-Learning-DAO/Dapp-Learning/blob/main/defi/Compound/contract/Compound%E5%90%88%E7%BA%A6%E9%83%A8%E7%BD%B2.md).(Forked compound only add access control, so only cTokenMinePool can access, which ensure the borrowIndex in cToken can't be changed unexpectedly.)

When complete deploying, copy cTokenDelegator & ComptrollerG1 address to replace the address in ./scripts/token.py, which is scripts of deploying and testing of cTokenMinePool.sol & MonkeyContract.sol, you can customize it to test more function.