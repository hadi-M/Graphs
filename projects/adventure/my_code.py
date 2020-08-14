from ipdb import set_trace as st


def get_empty_map(room_graph):
    traversed_map = dict()
    for k, v in room_graph.items():
        traversed_map[k] = {k:False for k, _ in v[1].items()}

    return traversed_map


def is_rooms_remaining(visited, room_graph):
    visited_set = set(visited)
    all_rooms_set = set(room_graph.keys())

    return bool(len(all_rooms_set - visited_set))


# def minimum_spanning_path(room_graph, node_id=0):
    # traversed_map = get_empty_map(room_graph)
    # back_nodes = dict()
    # path = []
    # current_node_id = 0
    # last_direction = None
    # while(is_rooms_remaining(traversed_map)):
    #     if last_direction is not None:  # means: it is not the first move
    #         back_direction = return_dict[last_direction]
    #         traversed_map[current_node_id].pop(back_direction)
    #         traversed_map[current_node_id]["back"] = back_direction
    #     node_directions = traversed_map[current_node_id]
    #     if node_directions != {}:
    #         next_direction = list(node_directions.keys())[0]
    #         is_checked = node_directions.pop(next_direction)
    #         st()
    #         # if next_direction in node_directions.keys(): # discovering is still needed
    #         if not is_checked:
    #             current_node_id = room_graph[current_node_id][1][next_direction]
    #             path.append(next_direction)
    #             last_direction = next_direction
        
                 
def minimum_spanning_path(room_graph, player, starting_vertex=0, visited=[]):

    return_dict = {
        "s": "n",
        "n": "s",
        "w": "e",
        "e": "w"
    }

    path = []

    for direction in player.current_room.get_exits():
        player.travel(direction)
        back_direction = return_dict[direction]

        if player.current_room.id not in visited:
            if not is_rooms_remaining(visited, room_graph):
                return path
            visited.append(player.current_room.id)
            path.append(direction)
            path = path + minimum_spanning_path(room_graph, player, player.current_room.id, visited)
            path.append(back_direction)
            player.travel(back_direction)
        else:
            player.travel(back_direction)
    
    return path