import java.util.*;

class Account {
    private String accountNumber;
    private String ownerName;
    private double balance;

    public Account() {
        this("0000", "Unknown", 0.0);
    }

    public Account(String accountNumber, String ownerName, double balance) {
        this.accountNumber = accountNumber;
        this.ownerName = ownerName;
        if (balance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative");
        }
        this.balance = balance;
    }

    public String getAccountNumber() {
        return accountNumber;
    }

    public String getOwnerName() {
        return ownerName;
    }

    public double getBalance() {
        return balance;
    }

    public void setOwnerName(String ownerName) {
        this.ownerName = ownerName;
    }

    protected void setBalance(double balance) {
        this.balance = balance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive");
        }
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdraw amount must be positive");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient balance");
        }
        balance -= amount;
    }

    public void display() {
        System.out.println("Account Number: " + accountNumber);
        System.out.println("Owner Name: " + ownerName);
        System.out.println("Balance: " + balance);
    }
}

class SavingsAccount extends Account {
    private double interestRate;

    public SavingsAccount(String accountNumber, String ownerName, double balance, double interestRate) {
        super(accountNumber, ownerName, balance);
        this.interestRate = interestRate;
    }

    public double calculateInterest() {
        return getBalance() * interestRate / 100;
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Interest Rate: " + interestRate + "%");
        System.out.println("Interest Earned: " + calculateInterest());
    }
}

class CurrentAccount extends Account {
    private double overdraftLimit;

    public CurrentAccount(String accountNumber, String ownerName, double balance, double overdraftLimit) {
        super(accountNumber, ownerName, balance);
        this.overdraftLimit = overdraftLimit;
    }

    @Override
    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdraw amount must be positive");
        }
        if (amount > getBalance() + overdraftLimit) {
            throw new IllegalArgumentException("Overdraft limit exceeded");
        }
        setBalance(getBalance() - amount);
    }

    @Override
    public void display() {
        super.display();
        System.out.println("Overdraft Limit: " + overdraftLimit);
    }
}

public class BankSystem {
    public static void main(String[] args) {
        List<Account> accounts = new ArrayList<>();

        accounts.add(new SavingsAccount("101", "Alice", 5000, 5));
        accounts.add(new CurrentAccount("102", "Bob", 2000, 1000));

        accounts.get(0).deposit(1000);
        accounts.get(1).withdraw(2500);

        for (Account acc : accounts) {
            System.out.println();
            acc.display();
        }
    }
}