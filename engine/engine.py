from __future__ import annotations
from typing import Callable, Any

import engine.operations as operations


class Node:
    def __init__(
        self,
        operation: Callable[[Any, Any], bool] = None,
        left: Node = None,
        right: Node = None,
        key: str = None,
        val=None,
        leaf: bool = False,
    ):
        self.operation = operation
        self.left = left
        self.right = right
        self.key = key
        self.val = val
        self.leaf = leaf


class AST:
    def __init__(self):
        self.root: Node = None
        self.operators: set = set([">", "<", ">=", "<=", "AND", "OR", "="])
        self.precendence: dict[str, int] = {
            ">": 10,
            "<": 10,
            ">=": 10,
            "<=": 10,
            "=": 10,
            "AND": 5,
            "OR": 5,
            "": 20,
        }

    def create_rule(self, rule: str)->Node:
        rule: str=rule.strip()
        rule: str = f"({rule})"
        stack: list = []

        close: list[int]= [-1] * len(rule)

        for i in range(len(rule)):
            if rule[i] == "(":
                stack.append(i)

            if rule[i] == ")":
                if len(stack) == 0:
                    raise ValueError("Invalid String")
                close[stack[-1]] = i
                stack.pop()
                

        def create(st: int, en: int)->Node:
            if st > en:
                return None

            r: str=rule[st: en+1].strip()
            if r == "":
                return None

            while rule[en]==' ':
                en-=1
                
            while rule[st]=='(' and close[st]>en:
                st+=1
            
            if rule[st]=='(' and rule[en]==')' and close[st]==en:
                return create(st+1, en-1)

            op: str = ""
            op_st: int = st
            op_en: int = en

            i: int = st

            while i <= en:
                if rule[i] == " ":
                    i += 1
                    continue

                if rule[i] == "(":
                    i = close[i] + 1
                    continue
                
                if i>en:
                    break

                next_space: int = rule.find(" ", i + 1)
                while next_space >= i and rule[next_space] == ")":
                    next_space -= 1
                cur: str = rule[i:next_space]

                if cur not in self.operators:
                    i = next_space + 1
                    continue

                if self.precendence[cur] < self.precendence[op]:
                    op = cur
                    op_st = i
                    op_en = next_space-1

                i = next_space + 1
                
            if op == "":
                r = rule[st:en+1].strip()
                if r[0] >= "a" and r[-1] <= "z":
                    return Node(key=r.strip(), leaf=True)
                if r[0] >= "0" and r[-1] <= "9":
                    return Node(val=float(r.strip()), leaf=True)
                if r[0] == """'""" and r[-1] == """'""":
                    return Node(val=r[1:-1].strip(), leaf=True)

            if op == " " or op == "":
                return None

            while rule[st]=='(' and close[st]>en:
                st+=1

            while en==" ":
                en-=1

            if rule[st] == "(" and rule[en] == ")" and close[st] == en:
                return Node(
                    operation=operations.func_map[op],
                    left=create(st+1, op_st - 2),
                    right=create(op_en + 2, en-1),
                )

            return Node(
                operation=operations.func_map[op],
                left=create(st, op_st - 2),
                right=create(op_en + 2, en),
            )

        return create(0, len(rule) - 1)
    
    def set_root(self, node: Node)-> None:
        self.root=node

    def combine_rules(self, rules: list[str])->Node:
        root: Node = None
        for i in range(len(rules)):
            node=self.create_rule(rules[i])
            
            if root is None:
                root=node
            else:
                par=Node(left=root, right=node, operation=operations.func_map['AND'])
                root: Node=par
        return root
            

    def evaluate_rule(self, data: dict)-> bool:
        if self.root is None:
            raise ValueError("root set to null")
        def dfs(node: Node):
            if node.leaf == True:
                if node.key is not None:
                    return data[node.key]
                else:
                    return node.val
                
            return node.operation(dfs(node.left), dfs(node.right))
        
        return dfs(self.root)
    