#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    temp = dir(hidden_4)
    [[temp[i][j] == '_' and temp[i][j+1] == '_' or print(temp[i])
        for j in range(len(temp[i]))] for i in range(len(temp))]
