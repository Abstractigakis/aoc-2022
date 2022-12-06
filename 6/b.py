
def f(data):
    for i in range(14, len(data)):
        ss = data[i-14:i]
        if len(ss) == len(set(ss)):
            return i

data = 'srjsssgppnssqzszmzjmjdmmqwqcwqccslsjswjssgbsgsnggqtqnnjznndtndnhddfldfdsfswsjsjjptjpttlwlccpnpgngcncnscncsnnwrwmwggsgdgssvbsstzsstqqrjqqlsqlsqscschhclhccznzcnnzzqppjbpjjqzzbwbqqzdqdjjqtjtbtgtqgtgdgwwsjjbwjjzssrsvsttgqtgglgplgpllcrcncssbrbgrbrllsqlsltthshrrnddwzdzdbbrppdvdqvvpvdvdsslbbmnbnjjrdrnntzzftzftttrsshpspvvrzzqzwzhzszbzjjwqwvqqglgflfwfrfprpddfvdffhzztwtppwwwztzsznzmnnbvbbtqqdhqdqdfffnjnmnlmljmlmnlnddzbbdgdqdnqqtjjtnthttvwwtrwwwgffqcfchfcfwcczhhgjhghpgpwgwffhghzghhtftntnnmlnmlmddqbbfwbfwbwvvfssrggptpltpllbcbzczzlccjgcgvcczjzvvvdtvdvqdqwdqdvdjvddjfdjjqmmfgfsftfzfwzwzfftmfmmqdqccjqcqwwflwlccpssvzzzbnbjnbjjgtgpttbwbrbwrwvrrwccgrgrvvpjvvznvvhddtdldpldppmlplltdllhqhpqhqqbpptgpgjgqjgjffvfdvdttsrsllhzlzrrdrnrjrddqbbjrrvrsstgsttjqjhjbhhnmndmmnrmnnrggmtgmmhshjjfqjjtqtstpstppggtzzrsrwwqffvzvzvqqggqsqtstszttpvtvvvddcncvncvchhnsnpsnnlmnnmqnqjjfwfccmwmbwbswbswwghhzrrptptbbjbtjjgdjgjrgrwgwlglblbnlnbbwnnpbnbmbtmtvvhjjlwlhhszslldwlwdllhjhghqghhqpplhhtjhhnhqhlhjhmmlhlmmrpptvvcczfcccwgcccpgpspdpccfhchffbjbzzwppfbbstbtltpllcssnnctnnqcqhhclhccvlvlffnjjwbwfbfttwvvdvnnnsrstrtmtfthtzzcvzvhzzpmpfpmmmwggdbdqdbbjnbbdqbbrnnnprrwbbcwbbpjjprjjzzvwwvrrthhqvhvnhhzmzszrszsjssclcjjbhjbhjbhjbjhhzbbzttnrnssrbrjbrjjmsmffdlflfzfbzzmtztdthdhldhlddnccgbbmtbbsbzsbzzcsszpzfffprfpfzfrzzhvhffsmmqtjwgjbzhnmrslrmgfjpqcllcgsjdhrshqtlgmqqtfmswfzwtnrswtzdjzclcfmltqgdhcsgvzrdltgfbtqclpppvbqnbqmlhmdbsjbwbdllzpnrwfhmnlgvdwsdjsznnhqzhwntjvcpzdrfwmwwdrttdvzspmbmqggmlmsvwgcjgpvcmplqwfjgpghnfpbctnfhcgngcbdmzhlpcnjpmczzsgfgrdftrzgvmmpdmgcrpcdrjsgczpfjnwpdjpntdngdjwctvcbsjmfwvtsrlhvpswppmfwrwzsbsgbjvljzqjjldmnqnmwsmqnmhmqhhttppbpqlvdcvdbhmbnjzztjrdjdzlvmbdrghtftwdpcwwblsjbgnzwtpztmtmnrpsvzfzncqmrvhcbqcvqvnlngdcllrqlbhjttnmjmhfhdzmjmplcfdqpmwblzsnmpczwcnggcwdvgnjcrrtmpwwqdqpvtbzpdbfnbfcfllntqjlslcsznjvzvsbntrtzwhcbtdmbmwttvhdvdtvrcmprcrrjlgsqddrsmwsrbtbpjrmlbrnsdrjfhjnqjtgjmhzjbjnprvmhtjcdbztwqmrlfflfmcslshtwmwhgvbdslgjhzjlglhllsdphlzngjfwfrlwpnqfhghnqhzhgrszbcwjvlrtmshntszsqplvfbccjwctgtfmqgqjdlgdbwhgvctqtcgfdwvqdwqzddmsbrpftzpqztgzbnplvhftmgpdthnrdhqbltbrmhpcqsfccmqzwmrbnbgbjspslwpjhdqspssqdtnssmjmvzwwfstgzzjrmfczdlznwqpdhbsjqddvffcgfhfdqdrlwcsgcsszdtpqbbsthpwbhdfzmgmcdggfcwcmzfjnfbzbccjhvwhbwfslnqnrwhgrwtlnmrmncnjtbjbdlmqsczppgbcmsdrwlrpjbgrmnhqqfhhsdhmdmpvvpjrnzsvzctmqhpzcvcjfgtlfvqvnvlnprmgrsvrrvtjfndqfsvqdsfbcwlbglmfhfhcfgqdfmclnzhdtppgzzsqgjqncqrbdhlhdjqwjpmbdnfmgdgwbwmnlngnmrhcgqwzvmbjzdvsspjwwdtpnvpftdlqlzfgtscfczsvbrtrqqpgqlvmrtddqplbzsswbgpdzpqfvqpqbndblghmdhmnctdnjbgglmrlvmrmsfgntfdwvqcvvlvbcnwrctvjqhmnsjqccwltbfqpqpmwsfvmnnfqmlmlcchqcdtbvqwcpptvfwrwtbdrlsgnwpmjgnwlprzqjlwqmtmjglbrzlgfbsghwqdmwhrcmfwdmzmflsbngtgndftdpzsqvgqdsfdhplmfcmwpbtvcdmpghmfwqjvhdhfpmbrqpvnbhlftgdtprlztrgnlcldfpjqjqdfrvqtcnzrtjcgzgsslzghlnfhwwjwzdsmpsczclrfmnqjvfmvsqpntsnnnlrfswqtrppzhqgjzlzvrrbhhfhchhvgztpgctcsgssvttszsrdwzwrbmwmspgqhmmfnzqqdbmnbltdmrsvqgddltwczbbjcmplncspgqgmzrndhttsrbvqbpbvhshfqrpqgmmdbhmmtccjcmntmpqhrvhnfnlqqbctsnfzjbphhqwmztgbhqqlbctbsfcszbggzrlcdhwddtjgtqhppzgjsqcddwjsngjrcdflmgwgfnzhjtcwgbqvpwmpgcpdwvqgswwfzcnjgmdpffmqczmsqgpthpmsjlwnrcbzrfshvwftzllwrmfccmlpjnmpjdfpcvjgjpznllmqjwpcflgqgdljtbbjvjlvhhmtvzfnjfnnwrvtlfdbhqphrjghtmlsrplqscsnvjvqdslsbsfzzrjfmchplzgjgdqvzhfphvsjfvnqlgmjfzhrdlmmvfntnzdvrnwqshsmtjnqmwzgpbbzszrsqcvlzjwnmgjhmfqrbvgmfqpswctmvpfcghvdqgstglmzvpfhzfzvhqqdmvrvrttlpwwhqgddzqlrvvdffqtznvlfgjhhmvbmtzjqnnhqzrtbzpqcwpngrdcndcgzwhzgtfwbmwbrpvvczczhwcqwsqzqbqvqftcswtcbzdbpccjhtwbpnwlwwwqwscptlwshrdbmmdcgrmpnnwgjwzszwwdwctfspbfqvdjqtrflshrqlbfgpnrmbszwjpcdzbggphgplcgvwljprzmtncsvfwqchttndhpnzmtdvtjqtcsddtqvcmztmjgwqvjhflrjjtnvfpjrnlvzvwvrpbhrzslmrqqzqhnzqnvtqppmncddphbwwsjczmphsrlltzndtqjgdlqgpnlfcvwntstmrgcrjzmmllpwldnwmwzpvzctmhszspcvtgnqthszzsmtdnzwtfddfctpjhscbqgwfpqmzpvqrzvtbrdjzrqprdgbpmzzfbgqcvcdtsfrffcpqwtvdwvtcqlcsdrzntgrhrspznndslmnvptlphpdqgbblfhmgbpmmfwqzlhvzshhpzgfjldqclngbcbrmmnqqvqmwdnjsglsggqfgjldqfbsqgtrwmpdffqlcwwlfhlpqfgwtssnjwzhgvtwqzmhmgwzwmcggmpmrzqrcsmflqsrbnzvdmjcdbnscstqrqhvddsbjpzwsvzswqhcqmgzlvfcnzjrrffzphmrvdbhqbrwpsfqvfqwhqhcgfvfsfttzcdsrjgjwcgvhllszmplmvgczqsbfldnbvrnqccbprjjdwhmqpdjjrnfdlhzdvlfmrldjlqclbjrrtjfsflphzdcdpfpr'
print(f(data))