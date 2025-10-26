# [2043. Simple Bank System](https://leetcode.com/problems/simple-bank-system/description/?envType=daily-question&envId=2025-10-24)

You have been tasked with writing a program for a popular bank that will automate all its incoming transactions (transfer, deposit, and withdraw). The bank has <code>n</code> accounts numbered from <code>1</code> to <code>n</code>. The initial balance of each account is stored in a **0-indexed**  integer array <code>balance</code>, with the <code>(i + 1)^th</code> account having an initial balance of <code>balance[i]</code>.

Execute all the **valid**  transactions. A transaction is **valid**  if:

- The given account number(s) are between <code>1</code> and <code>n</code>, and
- The amount of money withdrawn or transferred from is **less than or equal**  to the balance of the account.

Implement the <code>Bank</code> class:

- <code>Bank(long[] balance)</code> Initializes the object with the **0-indexed**  integer array <code>balance</code>.
- <code>boolean transfer(int account1, int account2, long money)</code> Transfers <code>money</code> dollars from the account numbered <code>account1</code> to the account numbered <code>account2</code>. Return <code>true</code> if the transaction was successful, <code>false</code> otherwise.
- <code>boolean deposit(int account, long money)</code> Deposit <code>money</code> dollars into the account numbered <code>account</code>. Return <code>true</code> if the transaction was successful, <code>false</code> otherwise.
- <code>boolean withdraw(int account, long money)</code> Withdraw <code>money</code> dollars from the account numbered <code>account</code>. Return <code>true</code> if the transaction was successful, <code>false</code> otherwise.

**Example 1:** 

```
Input

["Bank", "withdraw", "transfer", "deposit", "transfer", "withdraw"]
[[[10, 100, 20, 50, 30]], [3, 10], [5, 1, 20], [5, 20], [3, 4, 15], [10, 50]]
Output

[null, true, true, true, false, false]

Explanation

Bank bank = new Bank([10, 100, 20, 50, 30]);
bank.withdraw(3, 10);    // return true, account 3 has a balance of $20, so it is valid to withdraw $10.
                         // Account 3 has $20 - $10 = $10.
bank.transfer(5, 1, 20); // return true, account 5 has a balance of $30, so it is valid to transfer $20.
                         // Account 5 has $30 - $20 = $10, and account 1 has $10 + $20 = $30.
bank.deposit(5, 20);     // return true, it is valid to deposit $20 to account 5.
                         // Account 5 has $10 + $20 = $30.
bank.transfer(3, 4, 15); // return false, the current balance of account 3 is $10,
                         // so it is invalid to transfer $15 from it.
bank.withdraw(10, 50);   // return false, it is invalid because account 10 does not exist.
```

**Constraints:** 

- <code>n == balance.length</code>
- <code>1 <= n, account, account1, account2 <= 10^5</code>
- <code>0 <= balance[i], money <= 10^12</code>
- At most <code>10^4</code> calls will be made to **each**  function <code>transfer</code>, <code>deposit</code>, <code>withdraw</code>.

---

## Solution

```python
class Bank:

    def __init__(self, balance: List[int]):
        self.n = len(balance)
        self.accounts = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if 1 <= account1 <= self.n and 1 <= account2 <= self.n and self.accounts[account1-1] >= money:
            self.accounts[account1-1] -= money
            self.accounts[account2-1] += money
            return True
        else:
            return False

    def deposit(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n:
            self.accounts[account - 1] += money
            return True
        else:
            return False

    def withdraw(self, account: int, money: int) -> bool:
        if 1 <= account <= self.n and self.accounts[account - 1] >= money:
            self.accounts[account - 1] -= money
            return True
        else:
            return False
```