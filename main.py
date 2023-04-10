from cysimdjson import cysimdjson


def main(filepath: str):
    metadata_parser, gamedata_parser = cysimdjson.JSONParser(), cysimdjson.JSONParser()
    with open(filepath, 'rb') as file:
        metadata_raw, gamedata_raw = file.readline(), file.readline()
        stats = {'meta': {}, 'common': {}}
        metadata, gamedata = metadata_parser.parse(metadata_raw), gamedata_parser.parse(gamedata_raw)
        for key, value in metadata.items():
            if key not in stats['meta']:
                stats['meta'][key] = []
            value_type = type(value).__name__
            if value_type not in stats['meta'][key]:
                stats['meta'][key].append(value_type)
        for key, value in gamedata.at_pointer('/0/common').items():
            if key not in stats['common']:
                stats['common'][key] = []
            value_type = type(value).__name__
            if value_type not in stats['common'][key]:
                stats['common'][key].append(value_type)


main('6493223.json')
