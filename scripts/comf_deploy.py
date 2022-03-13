#!/usr/bin/python3

from brownie import CErc20Delegator, CErc20Delegate, WhitePaperInterestRateModel, ComptrollerG1, Unitroller, SimplePriceOracle, interface ,accounts



def main():
    
    dai = interface.daiInterface('0x6b175474e89094c44da98b954eedeac495271d0f')#DAI mainnet address
    # dai.mint(accounts[1],10000e18,{'from':'0x9759A6Ac90977b93B58547b4A71c78317f391A28'})
    # dai.mint(accounts[0],10000e18,{'from':'0x9759A6Ac90977b93B58547b4A71c78317f391A28'})
    ebal1 = accounts[0].balance()/1e18
    ebal2 = accounts[1].balance()/1e18
    print(f'\n')
    print(f'User1 ETH token balance is {ebal1}\n')
    print(f'User2 ETH token balance is {ebal2}\n')
    nbal1 = dai.balanceOf(accounts[0])
    nbal2 = dai.balanceOf(accounts[1])
    print(f'User1 Dai token balance is {nbal1/1e18}\n')
    print(f'User1 Dai token balance is {nbal2/1e18}\n')
    # comp = Comp.deploy(accounts[0],{'from':accounts[0]})
    spo = SimplePriceOracle.deploy({'from':accounts[0]})
    print(f'SimplePriceOracle address is : {spo.address}\n')
    uni = Unitroller.deploy({'from':accounts[0]})    
    print(f'Unitroller address is : {uni.address}\n')
    comtroo = ComptrollerG1.deploy({'from':accounts[0]})
    print(f'Comptroller address is : {comtroo.address}\n')
    intr = WhitePaperInterestRateModel.deploy(0.02e18, 0.15e18, {'from': accounts[0]})
    print(f'WhitePaperInterestRateModel address is : {intr.address}\n')
    dele = CErc20Delegate.deploy({'from': accounts[0]})  
    print(f'CErc20Delegate address is : {dele.address}\n')   
    uni._setPendingImplementation(comtroo.address, {'from': accounts[0]})   
    comtroo._become(uni.address, spo.address, 5e17, 20, False, {'from': accounts[0]})
    delo = CErc20Delegator.deploy(dai.address, uni.address, intr.address, 1e18, 'zDai token', 'zDAI', 18, accounts[0], dele.address, '0x', {'from': accounts[0]})
    print(f'zDai token contract address is {delo.address}\n')
    unicomptro = interface.ComptrollerG1(uni.address)
    print(f'Comptroller proxy has been set successful!!\n') 
    unicomptro._setCloseFactor(5e17,{'from':accounts[0]}) 
    unicomptro._setMaxAssets(20,{'from':accounts[0]})
    unicomptro._setPriceOracle(spo,{'from':accounts[0]})
    spo.setUnderlyingPrice(delo,1e18,{'from':accounts[0]})
    unicomptro._supportMarket(delo.address, {'from': accounts[0]})
    unicomptro._setCollateralFactor(delo,8e17,{'from':accounts[0]})
    # unicomptro.enterMarkets([delo.address], {'from': accounts[0]})   
    # unicomptro.enterMarkets([delo.address], {'from': accounts[1]})  
    print(f'Compound protocal has been set successfully!!\n')
    # dai.approve(delo.address, nbal1, {'from': accounts[0]})
    # dai.approve(delo.address, nbal2, {'from': accounts[1]})
    # allo1 = dai.allowance(accounts[0], delo.address)
    # allo2 = dai.allowance(accounts[1], delo.address)
    # print(f'User1 would like to supply {allo1/1e18} DAI to CToken Contract.\n')
    # print(f'User2 would like to supply {allo2/1e18} DAI to CToken Contract.\n')
    # delo.mint(allo1, {'from': accounts[0]})  
    # delo.mint(allo2, {'from': accounts[1]})
    # cbal1 = delo.balanceOf(accounts[0])
    # cbal2 = delo.balanceOf(accounts[1])
    # print(f'User1 hold cDai balance is : {cbal1/1e18}\n')
    # print(f'User2 hold cDai balance is : {cbal2/1e18}\n')

    # delo.redeemUnderlying(allo, {'from': accounts[0]})
    # b = dai.balanceOf(accounts[0])
    # print(f'Balance of cDai has been redeemed.\n And balance of dai is {b/1e18}\n')
    # delo.borrow(50e18, {'from': accounts[0]})
    # cbbal = delo.balanceOf(accounts[0])
    # print(f'Hold cDai balance is : {cbbal/1e18}\n')


