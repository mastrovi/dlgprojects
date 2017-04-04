#!/usr/bin/env python

rightsDict = {
    "CC BY":"https://creativecommons.org/licenses/by/4.0",
    "CC BY-SA":"https://creativecommons.org/licenses/by-sa/4.0",
    "CC BY-ND":"https://creativecommons.org/licenses/by-nd/4.0",
    "CC BY-NC":"https://creativecommons.org/licenses/by-nc/4.0",
    "CC BY-NC-SA":"https://creativecommons.org/licenses/by-nc-sa/4.0",
    "CC BY-NC-ND":"https://creativecommons.org/licenses/by-nc-nd/4.0",
    "In Copyright":"http://rightsstatements.org/vocab/InC/1.0/",
    "In Copyright - EU Orphan Work":"http://rightsstatements.org/vocab/InC-OW-EU/1.0/",
    "In Copyright - Educational Use Permitted":"http://rightsstatements.org/vocab/InC-EDU/1.0/",
    "In Copyright - Non-Commercial Use Permitted":"http://rightsstatements.org/vocab/InC-NC/1.0/",
    "In Copyright - Rights-holder(s) Unlocatable or Unidentifiable":"http://rightsstatements.org/vocab/InC-RUU/1.0/",
    "No Copyright - Contractual Restrictions":"http://rightsstatements.org/vocab/NoC-CR/1.0/",
    "No Copyright - Non-Commercial Use Only":"http://rightsstatements.org/vocab/NoC-NC/1.0/",
    "No Copyright - Other Known Legal Restrictions":"http://rightsstatements.org/vocab/NoC-OKLR/1.0/",
    "No Copyright - United States":"http://rightsstatements.org/vocab/NoC-US/1.0/",
    "Copyright Not Evaluated":"http://rightsstatements.org/vocab/CNE/1.0/",
    "Copyright Undetermined":"http://rightsstatements.org/vocab/UND/1.0/",
    "No Known Copyright":"http://rightsstatements.org/vocab/NKC/1.0/"
    }

qdcFieldsDict = {
    "dcterms:provenance":"dcterms_provenance",
    "dc:title":"dcterms_title",
    "dc:creator":"dcterms_creator",
    "dc:contributor":"dcterms_contributor",
    "dc:subject":"dcterms_subject",
    "dc:description":"dcterms_description",
    "dc:identifier":"dcterms_identifier",
    "dc:publisher":"dcterms_publisher",
    "dcterms:isShownAt":"dcterms_is_shown_at",
    "dc:date":"dc_date",
    "dcterms:temporal":"dcterms_temporal",
    "dcterms:spatial":"dcterms_spatial",
    "dc:format":"dc_format",
    "dcterms:isPartOf":"dcterms_is_part_of",
    "dc:rights":"dc_right",
    "dcterms:rightsHolder":"dcterms_rights_holder",
    "dcterms:bibliographicCitation":"dcterms_bibliographic_citation",
    "dlg:localRights":"dlg_local_right",
    "dc:relation":"dc_relation",
    "dc:type":"dcterms_type",
    "dcterms:medium":"dcterms_medium",
    "dcterms:extent":"dcterms_extent",
    "dc:language":"dcterms_language",
    "dlg:subjectPersonal":"dlg_subject_personal"
    }

nsDict = {
    'oai_dc':'http://www.openarchives.org/OAI/2.0/oai_dc/',
    'oai_qdc':'http://worldcat.org/xmlschemas/qdc-1.0/',
    'dcterms':'http://purl.org/dc/terms/',
    'dc':'http://purl.org/dc/elements/1.1/',
    'dlg':'http://dlg.org/local/elements/1.1/',
    'repox':'http://repox.ist.utl.pt'
    }