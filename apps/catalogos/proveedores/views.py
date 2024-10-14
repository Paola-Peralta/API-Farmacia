from django.shortcuts import render

 
    # def put(self, request, pk):
    #     try:
    #         proveedores = Proveedores.objects.get(pk=pk)
    #     except Proveedores.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "proveedor no encontrado"})
        
    #     serializer = ProveedoresSerializer(proveedores, data=request.data)        
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(status=status.HTTP_200_OK, data=serializer.data)
    
    # def delete(self, request, pk):
    #     try:
    #         proveedores = Proveedores.objects.get(pk=pk)
    #     except Proveedores.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "proveedor no encontrado"})
    
    #     proveedores.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    # def patch(self, request, pk):
    #     try:
    #         proveedores = Proveedores.objects.get(pk=pk)
    #     except proveedores.DoesNotExist:
    #         return Response(status=status.HTTP_404_NOT_FOUND, data={"error": "proveedor no encontrado"})
    
    #     serialize = ProveedoresSerializer(proveedores, data=request.data, partial=True)  # Permite actualizar solo los campos proporcionados
    #     serialize.is_valid(raise_exception=True)
    #     serialize.save()
    #     return Response(status=status.HTTP_200_OK, data=serialize.data)
