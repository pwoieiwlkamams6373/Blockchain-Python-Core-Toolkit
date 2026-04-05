# Python Blockchain Toolkit
> 一套基于 Python 实现的全场景区块链工具集，涵盖底层账本、密码学、共识算法、P2P 网络、钱包、NFT、DeFi、跨链、Layer2、DAO、链上分析等核心模块。所有代码均为原创独立设计，文件名与逻辑无重复，可直接用于学习、Demo 开发、GitHub 提交与项目展示。

---

## 项目信息
- **仓库名称**：`Python-Blockchain-Toolkit`
- **开发语言**：Python
- **应用方向**：区块链底层、Web3、加密货币、智能合约、分布式系统、链上数据分析

---

## 文件目录 & 功能说明（共 50 个）

### 1. 底层区块链与账本
1. **`Blockchain_Basic_Ledger.py`**
   实现最基础的区块链结构，包含创世区块、交易上链、区块挖矿、区块哈希、链结构校验等核心功能。

2. **`Block_Validator.py`**
   区块合法性验证工具，校验区块哈希、前一区块哈希、工作量证明有效性，保证链不可篡改。

3. **`Blockchain_Snapshot_Tool.py`**
   区块链状态快照工具，支持将整条链导出为 JSON 文件，用于节点备份与数据恢复。

4. **`Blockchain_Data_Export.py`**
   链数据导出工具，将区块高度、时间戳、交易数量导出为 CSV，方便可视化与数据分析。

5. **`Full_Node_Sync_Tool.py`**
   全节点同步逻辑，对比本地链与远程链高度，自动同步更长有效链。

6. **`Blockchain_Event_Logger.py`**
   区块链事件日志系统，记录出块、交易、异常等事件，持久化到日志文件便于排查。

---

### 2. 密码学与安全
7. **`Cryptography_ECDSA_Signer.py`**
   基于 SECP256k1 曲线的 ECDSA 签名与验签，是区块链地址与交易签名的标准算法。

8. **`Cryptography_AES_Encryptor.py`**
   AES 对称加密工具，用于链下敏感数据加密、钱包信息存储等场景。

9. **`Cryptography_Hash_Lock.py`**
   哈希锁实现，支持哈希时间锁定合约（HTLC），常用于跨链原子交换。

10. **`Zero_Knowledge_Proof_Simple.py`**
    简易零知识证明示例，实现不泄露原始信息即可证明拥有某秘密。

11. **`ZK_SNARKs_Verifier_Simple.py`**
    简化版 ZK-SNARKs 验证逻辑，用于隐私交易与链上匿名证明。

12. **`P2P_Message_Signer.py`**
    P2P 网络消息签名，防止节点间广播信息被篡改与伪造。

---

### 3. 共识机制
13. **`Consensus_PoW_Miner.py`**
    工作量证明（PoW）挖矿实现，支持难度调整、Nonce 计算、合法哈希校验。

14. **`Consensus_PoS_Validator.py`**
    权益证明（PoS）共识，按质押数量权重随机选择出块节点。

15. **`Consensus_DPoS_Delegate.py`**
    委托权益证明（DPoS），支持候选人注册、投票、选出顶级代理节点。

16. **`Consensus_PBFT_Basic.py`**
    实用拜占庭容错（PBFT）简化实现，适用于联盟链与许可链共识。

---

### 4. 钱包与账户系统
17. **`Wallet_Key_Generator.py`**
    钱包私钥、公钥、地址生成工具，模拟区块链标准地址生成流程。

18. **`Mnemonic_Generator.py`**
    助记词生成器，生成 BIP39 风格助记词，用于钱包备份与恢复。

19. **`Blockchain_Recovery_Tool.py`**
    钱包恢复工具，通过助记词恢复账户信息，模拟钱包软件逻辑。

20. **`Wallet_Balance_Batch_Checker.py`**
    批量余额查询工具，一次性查询多个地址在链上的资产余额。

---

### 5. 交易与区块优化
21. **`Transaction_Merkle_Tree.py`**
    默克尔树实现，用于交易聚合、默克尔根计算、轻节点证明。

22. **`Transaction_Priority_Queue.py`**
    交易优先队列，按 Gas 费从高到低排序，模拟矿工打包策略。

23. **`Block_Size_Optimizer.py`**
    区块大小优化器，在容量限制下选择最优交易集合打包。

24. **`Gas_Fee_Estimator.py`**
    Gas 费预估工具，区分普通转账与合约调用，给出合理 Gas 上限。

---

### 6. P2P 与分布式网络
25. **`P2P_Network_Node.py`**
    P2P 节点服务，支持节点监听、连接管理、消息广播与多线程处理。

26. **`CrossChain_Relay_Node.py`**
    跨链中继节点，实现链间消息转发、状态同步，是跨链桥核心组件。

---

### 7. 智能合约 & 链上逻辑
27. **`SmartContract_Simple_ERC20.py`**
    极简 ERC20 代币合约，实现发行、转账、余额查询等标准接口。

28. **`SmartContract_Multisig_Wallet.py`**
    多签钱包合约，支持多所有者共同签名，达到阈值才可执行转账。

29. **`SmartContract_Timelock.py`**
    时间锁合约，交易需等待锁定时间后才能执行，用于安全治理与延迟操作。

30. **`Web3_Contract_Caller.py`**
    模拟 Web3 合约调用工具，构造合约调用参数与返回结果解析。

---

### 8. NFT 相关
31. **`NFT_Metadata_Generator.py`**
    NFT 元数据生成工具，生成名称、描述、图片链接、属性并计算哈希。

32. **`NFT_Marketplace_Basic.py`**
    NFT 市场基础逻辑，支持 NFT 上架、挂单、购买、成交。

33. **`NFT_Staking_Reward.py`**
    NFT 质押挖矿，用户质押 NFT 可按天数获得奖励。

---

### 9. DeFi 去中心化金融
34. **`DeFi_Liquidity_Pool.py`**
    恒定乘积流动性池，实现添加流动性、代币兑换、滑点产生逻辑。

35. **`Staking_Reward_Calculator.py`**
    质押收益计算器，根据本金、APY、天数自动计算收益。

36. **`DeFi_Yield_Farmer.py`**
    收益耕作计算器，计算复利 APR，模拟流动性挖矿收益。

37. **`Defi_Slippage_Calculator.py`**
    DeFi 交易滑点计算，评估实际成交价格与预期价格偏差。

38. **`Bridge_Liquidity_Monitor.py`**
    跨链桥流动性监控，检查各资金池是否满足最低流动性要求。

---

### 10. 跨链 & Layer2
39. **`CrossChain_Asset_Bridge.py`**
    跨链资产桥，实现资产在原链锁定、目标链 mint、赎回销毁逻辑。

40. **`Layer2_Rollup_Basic.py`**
    Layer2 Rollup 基础实现，聚合大量 Layer2 交易生成统一证明上链。

---

### 11. DAO 与链上治理
41. **`DAO_Voting_System.py`**
    DAO 投票系统，支持提案创建、投票、结果统计，实现链上治理。

---

### 12. 预言机 & 外部数据
42. **`Oracle_Data_Fetcher.py`**
    区块链预言机，模拟获取链外价格数据，为合约提供喂价。

---

### 13. 高级结构与隐私
43. **`Blockchain_DAG_Structure.py`**
    DAG 结构区块链（有向无环图），不同于传统链式结构，支持并发单元。

44. **`Sharding_Chain_Manager.py`**
    区块链分片管理器，根据地址哈希路由到不同分片，提升 TPS。

45. **`Blockchain_Privacy_Mixer.py`**
    隐私混币工具，打乱交易输入来源，增强交易隐私性。

---

### 14. 链上分析 & 安全监控
46. **`Chain_Analysis_Tx_Tracker.py`**
    地址交易追踪器，遍历全链统计某地址所有转入转出记录与余额。

47. **`Blockchain_Anomaly_Detector.py`**
    链上异常交易检测器，识别大额转账、高频交易等风险行为。

48. **`Blockchain_Explorer_Basic.py`**
    简易区块链浏览器，支持按高度查块、最新块查询、链高获取。

49. **`IPFS_Content_Hash.py`**
    生成类 IPFS 的内容寻址哈希，用于去中心化存储与 NFT 资源定位。

50. **`Blockchain_Upgrade_Manager.py`**
    区块链协议升级管理器，支持版本号对比、软升级逻辑控制。

---

## 环境依赖安装
```bash
pip install ecdsa cryptography
