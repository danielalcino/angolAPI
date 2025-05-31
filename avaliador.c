#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

#define MAX_LINE 256
#define MAX_STACK 100

typedef struct {
    double items[MAX_STACK];
    int top;
} Stack;

void init(Stack *s) {
    s->top = -1;
}

int is_empty(Stack *s) {
    return s->top == -1;
}

int is_full(Stack *s) {
    return s->top == MAX_STACK - 1;
}

void push(Stack *s, double value) {
    if (!is_full(s)) {
        s->items[++s->top] = value;
    }
}

double pop(Stack *s) {
    if (!is_empty(s)) {
        return s->items[s->top--];
    }
    return 0;
}

double peek(Stack *s) {
    if (!is_empty(s)) {
        return s->items[s->top];
    }
    return 0;
}

int precedence(char op) {
    switch (op) {
        case '^': return 3;
        case '*': case '/': return 2;
        case '+': case '-': return 1;
        default: return 0;
    }
}

int is_operator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

int is_valid_char(char c) {
    return isdigit(c) || is_operator(c) || c == '(' || c == ')' || isspace(c);
}

int apply_operator(char op, double b, double a, double *result) {
    if (op == '/' && b == 0) return 0;
    switch (op) {
        case '+': *result = a + b; break;
        case '-': *result = a - b; break;
        case '*': *result = a * b; break;
        case '/': *result = a / b; break;
        case '^': *result = pow(a, b); break;
        default: return 0;
    }
    return 1;
}

int eval_expression(const char *expr, double *res, char *error) {
    Stack values, ops;
    init(&values);
    init(&ops);

    for (int i = 0; expr[i]; ++i) {
        char c = expr[i];
        if (!is_valid_char(c)) {
            strcpy(error, "Erro: Caracteres inválidos");
            return 0;
        }
        if (isspace(c)) continue;

        if (isdigit(c)) {
            push(&values, c - '0');
        } else if (c == '(') {
            push(&ops, c);
        } else if (c == ')') {
            int found = 0;
            while (!is_empty(&ops) && peek(&ops) != '(') {
                char op = pop(&ops);
                double b = pop(&values);
                double a = pop(&values);
                double r;
                if (!apply_operator(op, b, a, &r)) {
                    strcpy(error, "Erro: Divisão por zero");
                    return 0;
                }
                push(&values, r);
            }
            if (!is_empty(&ops) && peek(&ops) == '(') {
                pop(&ops);  // remove '('
                found = 1;
            }
            if (!found) {
                strcpy(error, "Erro: Parênteses desbalanceados");
                return 0;
            }
        } else if (is_operator(c)) {
            while (!is_empty(&ops) && precedence(peek(&ops)) >= precedence(c)) {
                char op = pop(&ops);
                double b = pop(&values);
                double a = pop(&values);
                double r;
                if (!apply_operator(op, b, a, &r)) {
                    strcpy(error, "Erro: Divisão por zero");
                    return 0;
                }
                push(&values, r);
            }
            push(&ops, c);
        }
    }

    while (!is_empty(&ops)) {
        char op = pop(&ops);
        if (is_empty(&values)) {
            strcpy(error, "Erro: Expressão malformada");
            return 0;
        }
        double b = pop(&values);
        double a = pop(&values);
        double r;
        if (!apply_operator(op, b, a, &r)) {
            strcpy(error, "Erro: Divisão por zero");
            return 0;
        }
        push(&values, r);
    }

    if (values.top != 0) {
        strcpy(error, "Erro: Expressão malformada");
        return 0;
    }

    *res = pop(&values);
    return 1;
}

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Uso: %s in.txt out.txt\n", argv[0]);
        return 1;
    }

    FILE *fin = fopen(argv[1], "r");
    FILE *fout = fopen(argv[2], "w");

    if (!fin || !fout) {
        printf("Erro ao abrir arquivos.\n");
        return 1;
    }

    char line[MAX_LINE];
    while (fgets(line, sizeof(line), fin)) {
        double result;
        char error[100] = "";
        line[strcspn(line, "\n")] = 0;  // remove \n

        if (eval_expression(line, &result, error)) {
            fprintf(fout, "%.0f\n", result);
        } else {
            fprintf(fout, "%s\n", error);
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
