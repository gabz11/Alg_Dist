class No:
    def __init__(self,id,bl=0):
        '''
        id = rótulo
        arr_links = array de nos conectados
        bl = aresta bidirecional 0 ou 1
        @param: id,bl
        @return: No
        '''
        self.id = id
        self.arr_links = []
        self.bl = bl
    
    def conectar(no_link):
        # cria aresta/link entre nos
        if self.bl == 1:
            No = self.__init__
            self.arr_links.append(no_link)
            no_link.arr_links.append(No)
        else:
            self.arr_links.append(no_link)



    