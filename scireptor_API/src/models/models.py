from . import db


from sqlalchemy.inspection import inspect

class Serializer(object):

    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}

    @staticmethod
    def serialize_list(l):
        return [m.serialize() for m in l]
class Sample(db.Model):
    """Data model for samples."""

    __tablename__ = 'sample'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    sample_id = db.Column(db.Integer,primary_key=True)
    donor_id = db.Column(db.Integer, index=True, unique=True, nullable=False)
    tissue = db.Column(db.String(45), index=False, unique=False, nullable=False)
    sampling_date = db.Column(db.DateTime,
                                  index=False,
                                  unique=False,
                                  nullable=True)
    add_sample_info = db.Column(db.String(100),
                                    index=False,
                                    unique=False,
                                    nullable=False)
class Flow(db.Model):
    __tablename__='flow'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    flow_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column( db.Integer, db.ForeignKey('sequences.event_id'))
    channel_id = db.Column(db.Integer, index=True, unique= True, nullable= False)
    value = db.Column(db.Float, index=True, nullable=False)
    cell = db.relationship('Sequence', backref= 'flow')

class Rearrangement(db.Model):
    __tablename__='dervied_segment_rearrangements'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    rearrangement_id=db.Column(db.Integer, primary_key=True)
    event_id= db.Column(db.Integer, db.ForeignKey('sequences.event_id'))
    v_call=db.Column(db.String(100), index= True, unique= True, nullable=  False)
    d_call=db.Column(db.String(100), index= True, unique= True, nullable=  False)
    j_call=db.Column(db.String(100), index= True, unique= True, nullable=  False)
    c_call=db.Column(db.String(100), index= True, unique= True, nullable=  False)
    locus=db.Column(db.String(100), index= True, unique= True, nullable=  False)
    igblast_productive = db.Column(db.String(100), index=True, unique=True, nullable=False)
    vdj = db.relationship('Sequence', backref='rearrangement')

class Sequence(db.Model):
    __tablename__ = 'sequences'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    seq_id= db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, index= True, unique= True, nullable=  False )
    consensus_rank = db.Column(db.Integer, unique= True, nullable=  False )
    locus = db.Column(db.String(2), index=True,
                         unique=True,
                         nullable=False)
    length = db.Column(db.Integer, index= True, unique= True, nullable= False)
    orient = db.Column(db.String(1), index= True, unique= True, nullable=  False)
    igblast_productive = db.Column(db.Integer, unique= True, nullable=  False )
    seq= db.Column(db.String(2000), index=True,
                         unique=True,
                         nullable=False)
    event_id = db.Column(db.Integer, unique= True, nullable=  False)

class Event(db.Model):
    __tablename__ = 'event'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    event_id= db.Column(db.Integer, primary_key=True)
    sort_id = db.Column(db.Integer, index= True, unique= True, nullable=  False)
    relation = db.relationship('Sequence', backref='event')

class Sort(db.Model):
    __tablename__ = 'sort'
    sort_id = db.Column(db.Integer,  primary_key=True)
    population = db.Column(db.String(10), index= True, unique= True, nullable=  False)
    relation = db.relationship('Event', backref= 'sort')

class SequenceInfo(db.Model):
    __tablename__ = 'sequencing_run'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    sequencing_run_id= db.Column(db.Integer, primary_key=True)
    experiment_id = db.Column(db.String(100), index= True, unique= True, nullable=  False)
    name = db.Column(db.String(100), index= True, unique= True, nullable=  False)

class Donor(db.Model):
    __tablename__ = 'donor'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    donor_id = db.Column(db.Integer, primary_key=True)
    donor_identifier = db.Column(db.String(100), index= True, unique= True, nullable=  False)
    species_id = db.Column(db.String(100), index=True, unique=True, nullable=False)
    strain = db.Column(db.String(100), index= True, unique= True, nullable=  False)
    add_donor_info = db.Column(db.String(2000), index= True, unique= True, nullable=  False)
    relation_sample = db.relationship('Sample', backref='donor')

class CDR(db.Model):
    __tablename__ = 'CDR_FWR'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    seq_id = db.Column(db.Integer,  db.ForeignKey('rearrangement.seq_id'))
    CDR_FWR_id = db.Column(db.Integer, primary_key=True)
    region= db.Column(db.String(100), index= True, unique= True, nullable=  False)
    dna_seq = db.Column(db.String(2000), index=True,
                         unique=True,
                         nullable=False)
    prot_seq = db.Column(db.String(2000), index=True,
                         unique=True,
                         nullable=False)
    relation = db.relationship('Rearrangement', backref='cdr')

class VDJ(db.Model):
    __tablename__ = 'VDJ_segments'
    __table_args__ = {'mysql_row_format': 'DYNAMIC'}
    VDJ_segments_id = db.Column(db.Integer,  primary_key=True)
    seq_id = db.Column(db.Integer, db.ForeignKey('rearrangement.seq_id'))
    type= db.Column(db.String(100), index= True, unique= True, nullable=  False)
    locus = db.Column(db.String(2), index=True,
                         unique=True,
                         nullable=False)
    igblast_rank = db.Column(db.Integer, index=True,
                         unique=True,
                         nullable=False)
    name= db.Column(db.String(100), index= True, unique= True, nullable=  False)
    eval = db.Column(db.Integer,  index= True, unique= True, nullable=  False)
    score = db.Column(db.Integer,  index= True, unique= True, nullable=  False)
    VDJ_id= db.Column(db.Integer,  index= True, unique= True, nullable=  False)
    relation = db.relationship('Rearrangement', backref='vdj')


