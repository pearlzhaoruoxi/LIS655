# Acquisition Plan

## Workflow

### Working with Producers
Exemplar knitting data files were identified on ravelry.com based on their uniqueness, their use of features of the knitting machine, and the existence of images and/or forum posts that documented the finished knitwear. The creator of each data file was contacted and asked to sign a deed of gift to grant the Museum a non-exclusive license to preserve and make accessible the data files and their documentation.

### Receiving SIP
Each SIP was saved to a separate folder, based on the pattern name. The .dat file and images were downloaded using a browser, and a WARC of the website was created using Web Recorder. The images and WARC were placed in a subfolder labeled documentation. The deed of gift was placed in a subfolder labeled license.

### Quality Assurance
After collecting all of the objects, each SIP was reviewed to make sure that all supporting material related to the .dat file.

### Generating AIP
The decision was made to process the SIPs as a single AIP. All collected SIPs were placed in a single folder. Technical metadata was generated for all of the objects using DROID and the resulting report was stored in the AIP. Finally, the AIP was bagged using bagit.py in order to generate fixity information for long-term storage.

### Generating Description
Each object received its own record in the Museum’s collection management system. The records recorded the following:
* Administrative: accession number
* Descriptive: original name of the pattern, the creator of the work
* Technical: machine and yarn needed to execute the pattern

The accession numbers and associated name and creator of the works were exported to a spreadsheet. This spreadsheet was added to the AIP before bagging.


## Reflection
While a number of potential objects were identified for potential collection, Ravelry members often did not make their data files available for download. This greatly reduced the hoped-for scope of the collection from 30 objects down to 5. In addition, because Ravelry is a password-protected site, I contacted the site for permission to collect its web pages.

When I used DROID to generate the AIP, it successfully identified all of the documentation files. However, it only identified the .dat files as generic data files, not as files specifically made to interact with the Brother KH-930. If possible, it would be useful to update the PRONOM registry with a signature that can identify the formats to this level, although it’s not clear how much work this would take.

While recording the metadata, it became clear that the actual creation of this knitwear was very dependent on the availability of certain types and colors of yarn. While the initial goal of this collection was to be able to reproduce the knitwear on exhibit, the fact that the exact yarn may or may not be available in the future might hamper the authenticity of an exhibit.

Finally, in terms of scaling this acquisition process, the negotiation with each creator took far more time than expected and would likely be a significant barrier to collecting larger amounts of this material. If possible, it would be more useful to find single creators with large collections so that we can streamline the rights process. 




