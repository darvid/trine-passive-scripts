"""Make class trainers vendors and populate them with glyphs."""
from constants import CLASS_NAMES, ChrClasses, NpcFlag, Trainer
from models.world import CreatureTemplate, ItemTemplate, NpcVendor


def get_trainer(session, class_name):
    trainer = session.query(CreatureTemplate).\
        filter(CreatureTemplate.name.like(class_name + " Trainer%")).one()
    if class_name == "Death Knight":
        if not trainer.npcflag & NpcFlag.TRAINER == NpcFlag.TRAINER:
            trainer.name = "Death Knight Trainer"
            trainer.npcflag += NpcFlag.TRAINER + NpcFlag.CLASS_TRAINER
            trainer.trainer_type = Trainer.TYPE_CLASS
            trainer.trainer_class = ChrClasses.DEATH_KNIGHT.id
            trainer.npcflag += NpcFlag.CLASS_TRAINER
            session.merge(trainer)
    return trainer


def get_all_glyphs(session, class_id=None):
    query = session.query(ItemTemplate).\
        filter(ItemTemplate.name.like("Glyph Of%")).\
        filter(ItemTemplate.name != "Glyph of Azora")
    if class_id is not None:
        query = query.filter(ItemTemplate.AllowableClass == class_id)
    for glyph in query.order_by(ItemTemplate.name):
        yield glyph


def merge(session):
    # store item slot numbers, since they aren't autoincrement in the db
    slots = dict(zip(CLASS_NAMES, [0] * 10))
    for class_name in CLASS_NAMES:
        trainer = get_trainer(session, class_name)
        # only modify npcflag if trainer isn't already a vendor, to avoid
        # conflicts with a custom npcflag
        if not trainer.npcflag & NpcFlag.VENDOR == NpcFlag.VENDOR:
            trainer.npcflag += NpcFlag.VENDOR
        if not trainer.npcflag & NpcFlag.GOSSIP == NpcFlag.GOSSIP:
            trainer.npcflag += NpcFlag.GOSSIP
        # delete all items associated with this npc
        session.query(NpcVendor).\
            filter(NpcVendor.entry == trainer.entry).delete()
        # get the base 2 representation of the class that's used in the db
        c_id = ChrClasses.find_class(class_name, method="display_name").binary
        # filter all glyphs by class
        for glyph in get_all_glyphs(session, c_id):
            session.merge(NpcVendor(entry=trainer.entry, item=glyph.entry,
                slot=slots[class_name]))
            slots[class_name] += 1
