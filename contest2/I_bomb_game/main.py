def bomb_in_boundary_count(field, horizont_boundry, vertical_boundary):
    count = 0
    for i in range(horizont_boundry[0], horizont_boundry[1] + 1):
        for j in range(vertical_boundary[0], vertical_boundary[1] + 1):
            if field[i][j] == '*':
                count += 1
    return count


def get_boundary_for_edge(squere_pos_dim, len_of_dim):
    if squere_pos_dim == 0:
        boundary = (0, 1)
    elif squere_pos_dim == len_of_dim - 1:
        boundary = (len_of_dim - 2, len_of_dim - 1)
    else:
        boundary = (squere_pos_dim - 1, squere_pos_dim + 1)
    return boundary


def edge_bomb_count(field, square_pos_h, square_pos_v, N, M):
    horizont_boundry = get_boundary_for_edge(square_pos_h, N)
    vertical_boundary = get_boundary_for_edge(square_pos_v, M)
    count = bomb_in_boundary_count(field, horizont_boundry, vertical_boundary)
    return count


def create_field(N, M, bombs):
    field = []
    for i in range(N):
        field.append([0]*M)
        for j in range(M):
            if (i + 1, j + 1) in bombs:
                field[i][j] = '*'

    for i in range(N):
        for j in range(M):
            if field[i][j] == '*':
                continue
            elif (i in [0, N-1]) or (j in [0, M-1]):
                field[i][j] = edge_bomb_count(field, i, j, N, M)
            else:
                field[i][j] = bomb_in_boundary_count(field, (i - 1, i + 1), (j - 1, j + 1))
    return field


def print_field(field, N, M):
    str_field_h_list = []
    for i in range(N):
        for j in range(M):
            str_field_h_list.append(str(field[i][j]))
        str_field_h = ' '.join(str_field_h_list)
        print(str_field_h)
        str_field_h_list = []


N, M, K = list(map(int, input().split()))
bombs = []
for i in range(K):
    bomb = tuple(map(int, input().split()))
    bombs.append(bomb)

ans = create_field(N, M, bombs)
print_field(ans, N, M)

