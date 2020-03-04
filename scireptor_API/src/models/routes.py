from flask import  jsonify,request, json
from flask import current_app as app
from .models import db, Sample, Rearrangement, CDR, Sequence, Event, Sort, Donor, SequenceInfo
from .views import *

@app.route('/api/test/cells', methods=['GET', 'POST'])
def get_test_cells():
    if 'cell_id' in request.args:
        cells = db.session.query(Event.event_id, Sequence.seq_id, Sort.sort_id).join(Sort, Event.sort_id == Sort.
                                                                                     sort_id).\
            join(Sequence, Event.event_id == Sequence.event_id).filter(
            Event.event_id == request.args['cell_id']).order_by(Sequence.event_id)
        
        return create_response_cell(cells)
    else:
        cells = db.session.query(Event.event_id, Sequence.seq_id, Sort.sort_id).join(Sort,
                Event.sort_id == Sort.sort_id).join(Sequence, Event.event_id == Sequence.event_id).\
            order_by(Sequence.event_id)
        
        return create_response_cell(cells)

@app.route('/api/test/cell/<int:cell_id>', methods=['GET', 'POST'])
def get_test_cell(cell_id):
    cells= db.session.query(Event.event_id, Sequence.seq_id, Sort.sort_id).join(Sort, Event.sort_id == Sort.sort_id).\
        join(Sequence, Event.event_id == Sequence.event_id).filter(Event.event_id==cell_id).order_by(Sequence.event_id)
    
    return create_response_cell(cells)

@app.route('/api/test/repertoires', methods=['GET', 'POST'])
def get_test_repertoires():
    samples= db.session.query(Sample.sample_id,Sample.tissue, Sort.sort_id, Donor.donor_identifier, Donor.donor_id,
                              Donor.strain, SequenceInfo.name, Donor.add_donor_info, Donor.species_id,
                              SequenceInfo.experiment_id).join(Sample, Sample.sample_id == Sort.sort_id).join(
        Donor, Donor.donor_id == Sample.donor_id).join(SequenceInfo, SequenceInfo.sequencing_run_id==
                                                       SequenceInfo.sequencing_run_id)
    if 'repertoire_id' in request.args:
        sample_query= samples.filter(Sort.sort_id == request.args['repertoire_id'])
        return create_response_repertoire(sample_query)
    else:
        sample_query = samples
        return create_response_repertoire(sample_query)

@app.route('/api/test/repertoire/<int:repertoire_id>', methods=['GET', 'POST'])
def get_test_repertoire(repertoire_id):
    samples = db.session.query(Sample.sample_id, Sample.tissue, Sort.sort_id, Donor.donor_identifier, Donor.donor_id,
                               Donor.strain, SequenceInfo.name, Donor.add_donor_info, Donor.species_id,
                               SequenceInfo.experiment_id).join(Sample, Sample.sample_id == Sort.sort_id).join(
        Donor, Donor.donor_id == Sample.donor_id).join(SequenceInfo, SequenceInfo.sequencing_run_id ==
                                                       SequenceInfo.sequencing_run_id).filter(Sort.sort_id == repertoire_id)
    return create_response_repertoire(samples)
@app.route('/api/test/rearrangements', methods=['POST', 'GET'])
def get_reaarangements():
        queries= db.session.query(Rearrangement.rearrangement_id, Rearrangement.v_call, Rearrangement.d_call,
                    Rearrangement.igblast_productive, Rearrangement.c_call, Rearrangement.locus,
                    Rearrangement.j_call, Rearrangement.event_id, CDR.dna_seq, CDR.prot_seq).join(
        CDR, CDR.seq_id == Rearrangement.rearrangement_id).filter(CDR.region == "CDR3").order_by(Rearrangement.event_id)
        if 'rearrangement_id' in request.args:
            rearrangements = queries.filter(Rearrangement.rearrangement_id ==request.args['rearrangement_id'])
            return create_response_rearrangement(rearrangements)
        elif 'v_call' in request.args:
            rearrangements = queries.filter(Rearrangement.v_call == request.args['v_call'])
            return create_response_rearrangement(rearrangements)
        elif 'd_call' in request.args:
            rearrangements = queries.filter(Rearrangement.d_call == request.args['d_call'])
            return create_response_rearrangement(rearrangements)
        elif 'c_call' in request.args:
            rearrangements = queries.filter(Rearrangement.c_call == request.args['c_call'])
            return create_response_rearrangement(rearrangements)
        elif 'locus' in request.args:
            rearrangements = queries.filter(Rearrangement.locus == request.args['locus'])
            return create_response_rearrangement(rearrangements)
        else:
            return create_response_rearrangement(queries)

@app.route('/api/test/rearrangement/<int:re_id>', methods=['GET', 'POST'])
def get_reaarangement(re_id):
    rearrangement = db.session.query(Rearrangement.rearrangement_id, Rearrangement.v_call, Rearrangement.d_call,
                                     Rearrangement.igblast_productive, Rearrangement.c_call, Rearrangement.locus,
                                     Rearrangement.j_call, Rearrangement.event_id, CDR.dna_seq,CDR.prot_seq).\
        join(CDR, CDR.seq_id==Rearrangement.rearrangement_id).filter(CDR.region == "CDR3").\
        filter(Rearrangement.rearrangement_id == re_id)
    
    create_response_rearrangement(rearrangement)
