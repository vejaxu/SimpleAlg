#include <iostream>
using namespace std;

// 定义循环链表节点
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// 创建循环链表
Node* createCircularLinkedList(int n) {
    Node* head = new Node(1);
    Node* prev = head;
    for (int i = 2; i <= n; ++i) {
        prev->next = new Node(i);
        prev = prev->next;
    }
    prev->next = head; // 形成循环
    return head;
}

// 解决约瑟夫环问题
void josephusProblem(Node* head, int k) {
    Node* current = head;
    Node* prev = nullptr;
    while (current->next != current) {
        // 寻找第 k 个节点
        for (int i = 1; i < k; ++i) {
            prev = current;
            current = current->next;
        }
        // 删除第 k 个节点
        prev->next = current->next;
        Node* temp = current;
        current = current->next;
        delete temp;
    }
    cout << "Last person left standing: " << current->data << endl;
}

int main() {
    int n = 7; // 总人数
    int k = 3; // 每次数数的步长
    Node* head = createCircularLinkedList(n);
    josephusProblem(head, k);
    return 0;
}
