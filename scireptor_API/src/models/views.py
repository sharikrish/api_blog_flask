from flask import jsonify
def create_response_cell(cells):
    cells_list = []
    for x in cells:
        groups = {
            'cell_id': str(x[0]),
            'rearrangement_id': str(x[1])
        }
        cells_list.append(groups)
    cell_list = []
    for index in set(item['cell_id'] for item in cells_list):
        sub = {
            'cell_id': index,
            'rearrangement_id': [item["rearrangement_id"] for item in cells_list if item['cell_id'] == index],
            'virtual': bool(False)}
        cell_list.append(sub)
    return jsonify({'Cell': cell_list})

def create_response_rearrangement(rearrangement):
    rearrangement_ls = []
    for x in rearrangement:
        sub = {'rearrangement_id': x[0],
               "productive": x[3],
               "v_call": x[1],
               "d_call": x[2],
               "j_call": x[6],
               "c_call": x[4],
               "locus": x[5],
               "cell_id": x[7],
               "junction": x[8],
               "junction_aa": x[9]}
        rearrangement_ls.append(sub)
    return jsonify({'Rearrangements': rearrangement_ls})
def create_response_repertoire(repertoire):
    repertoire_ls = []
    for i in repertoire:
        fields_info = i[7].split(",")
        sex = fields_info[0].split("=")
        age = fields_info[1].split("=")
        groups = {'repertoire_id': i[2],
              "Sample":
                  {"sample_id": i[0],
                   "tissue": i[1]},
              "Subject":
                  {"subject_id": i[4],
                   "organism": i[8],
                   "strain": i[5],
                   "age": age[1],
                   "sex": sex[1]},
              "Study":
                  {"study_id": i[9],
                   "study_title": i[6]}}
        repertoire_ls.append([groups])
    return jsonify(({'Repertoire': repertoire_ls}))